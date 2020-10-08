from sense_hat import SenseHat
from gps3 import gps3
import requests
import json
import time
import threading
from datetime import datetime
import struct
import sys
import bz2
import os

gpsData = {}
sensorData = {}
DATA_TEMP_MAX = 1
MIMETYPE = 'application/dmscb'
CONNECTION_RETRY = 2
DATA_TEMP_ARRAY_MAX = 3  # バッファ数
data_temp = [bytes()] * DATA_TEMP_ARRAY_MAX
data_temp_array_index = 1
data_temp_index = 0
data_send_flag = [False] * DATA_TEMP_ARRAY_MAX
data_send_last = 0

gpsData["gps_lat"] = 0.0
gpsData["gps_lon"] = 0.0
gpsData["gps_alt"] = 0.0
gpsData["gps_speed"] = 0.0


def getgps():
    global gpsData
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()

    for new_data in gps_socket:
        if new_data:

            data_stream.unpack(new_data)
            data_temp_gps = {}  # 一時格納用

            lat = data_stream.TPV['lat']
            lon = data_stream.TPV['lon']
            if (lat != 'n/a' and lon != 'n/a'):
                data_temp_gps["gps_lat"] = float(lat)
                data_temp_gps["gps_lon"] = float(lon)
            else:
                data_temp_gps["gps_lat"] = 0.0
                data_temp_gps["gps_lon"] = 0.0

            alt = data_stream.TPV['alt']
            if (alt == 'n/a'):
                data_temp_gps["gps_alt"] = 0.0
            else:
                data_temp_gps["gps_alt"] = float(alt)
            speed = data_stream.TPV['speed']
            if (speed == 'n/a'):
                data_temp_gps["gps_speed"] = 0.0
            else:
                data_temp_gps["gps_speed"] = float(speed)

        gpsData = data_temp_gps


def getSensors():
    global sensorData
    sense = SenseHat()
    sense.clear()

    while True:

        sensorData["temprature"] = sense.get_temperature()
        # sensorData["pressure"] = sense.get_pressure()
        sensorData["humidity"] = sense.get_humidity()
        acceleration = sense.get_accelerometer_raw()
        sensorData["acceleration_x"] = acceleration['x']
        sensorData["acceleration_y"] = acceleration['y']
        sensorData["acceleration_z"] = acceleration['z']

        time.sleep(0.2)


def uploadSensorValues():
    global sensorData, data_send_last, data_temp, data_temp_array_index, data_temp_index, data_send_flag
    send_target_index = 0  # 次に出力するバッファ番号

    url = 'http://192.168.30.110:3000'
    # url = 'http://133.19.62.11:9200/hakuba_sencing_info_3/a'
    # url = 'http://192.168.100.121:20000/mnt/data/sensor1/'
    sense = SenseHat()
    while True:
        if(data_send_last < DATA_TEMP_ARRAY_MAX - 1):
            send_target_index = data_send_last + 1
        else:
            send_target_index = 0

        if(data_send_flag[send_target_index] == True):

            print(send_target_index)
            outdatatmp = data_temp[0]
            print(outdatatmp)

            # サーバへの送信
            stime = time.time()
            response = None
            sensdsucess = False
            for i in range(1, CONNECTION_RETRY + 1):
                try:
                    response = requests.post(url, json=outdatatmp, timeout=(2.0, 8.0))
                except Exception as e:
                    print("サーバ送信エラー" + str(e) + " retry:{i}/{max}:wait{w}s".format(i=i, max=CONNECTION_RETRY, w=i * 5))
                    time.sleep(i * 5)
                else:
                    sendsucess = True
                    print("SEND_SUCCES")
                    break
            if(sendsucess):
                # print(response.status_code)
                print(response.content)
                # デバック用（送信できたらLEDが光る）
                sense.clear()
                sense.set_pixel(0, 0, [0, 0, 255])
            else:
                print("送信失敗、データは破棄されます")
                etime = time.time()

                print("送信にかかった時間：" + str(etime - stime))
            data_send_flag[send_target_index] = False
            data_send_last = send_target_index

        time.sleep(0.1)


def main_program():
    global sensorData, data_temp_array_index, data_temp_index, data_send_flag, data_tmp
    beginTime = 0
    time.sleep(1)
    while True:
        cuTime = time.time()
        if cuTime - beginTime >= 0.1:
            beginTime = cuTime
            sensorData_ = sensorData
            print(sensorData_)
            gpsData_ = gpsData
            SensorData = {}
            SensorData["time"] = cuTime
            # SensorData.append(gpsData_["gps_lat"])
            # SensorData.append(gpsData_["gps_lon"])
            # SensorData.append(gpsData_["gps_alt"])
            # SensorData.append(gpsData_["gps_speed"])
            SensorData["accel_x"] = sensorData_["acceleration_x"]
            SensorData["accel_y"] = sensorData_["acceleration_y"]
            SensorData["accel_z"] = sensorData_["acceleration_x"]

            data_temp.append(SensorData)

            data_temp_index += 1

            time_temp = time.time()
            print("データ数: " + str(data_temp_index))

            # 現在のバッファがいっぱいになったとき
            if data_temp_index >= DATA_TEMP_MAX:
                data_send_flag[data_temp_array_index] = True
                data_temp_index = 0
                print("データ配列数: " + str(data_temp_array_index))
                data_temp_array_index += 1
                # 最後のバッファに到達した場合
                if (data_temp_array_index >= DATA_TEMP_ARRAY_MAX):
                    data_temp_array_index = 0

                data_temp[data_temp_array_index] = bytes()


if __name__ == '__main__':
    sensethread = threading.Thread(target=getSensors, args=())
    sensethread.start()
    # gpsthread = threading.Thread(target=getgps, args=())
    # gpsthread.start()
    time.sleep(1)
    sendthread = threading.Thread(target=uploadSensorValues, args=())
    sendthread.start()
    main_program()
