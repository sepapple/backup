from pybleno import *
import random
import time
from gps3 import gps3
import struct
from sense_hat import SenseHat
import requests
import json
import threading
import sys
import os
from web3 import Web3
import time
from concurrent.futures import ThreadPoolExecutor



bleno = Bleno()

NAME = 'Raspberry-pi'
APPROACH_SERVICE_UUID = '19B10010-E8F2-537E-4F6C-D104768A1214'
WRITE_CHARACTERISTIC_UUID = '19B10011-E8F2-537E-4F6C-D104768A1214'
NOTIFY_CHARACTERISTIC_UUID = '19B10012-E8F2-537E-4F6C-D104768A1214'

#IDを管理する変数
peripheral_ID = 10
android_ID = 0
connection_ID = 0

#センサデータ
send_data = [] #送信するデータ
datacount = 0
chunks = 30 #何個のデータをまとめて送るかを決める変数
accel_x = [0,0,0,0,0,0,0,0,0,0]
accel_y = [0,0,0,0,0,0,0,0,0,0]
accel_z = [0,0,0,0,0,0,0,0,0,0]
lat = 0
lon = 0

current_time = time.time()
startflag = True
connectionflag = False
STANDARD_GRAVITY = 9.80665
TRANSMISSIOM_TIME = 1000

#ファイルからデータの抽出
f =  open('/home/pi/code/webinterface/CarContract.json','r')
jsonData = json.load(f)
contract_address = jsonData['networks']['15']['address']
contract_abi = jsonData['abi']

#ブロックチェーン関係
w3 = Web3(Web3.HTTPProvider('http://192.168.30.30:8545'))
myContract = w3.eth.contract(address=contract_address,abi=contract_abi)
URL = 'http://192.168.30.30:8500/bzz:/'  #SwarmのURL

#Characteristicの設定
class NotifyCharacteristic(Characteristic):
        
    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': NOTIFY_CHARACTERISTIC_UUID,
            'properties': ['notify'],
            'value': None
        })

        self._value = 0
        self._updateValueCallback = None


    def onSubscribe(self, maxValueSize, updateValueCallback):
        global connection_ID
        print('NotifyCharacteristic - onSubscribe')
        surveillancethread = threading.Thread(target=Surveillance, args=())
        surveillancethread.start()
        connection_ID = round(random.random()*1000000000)
        self._updateValueCallback = updateValueCallback

    def onUnsubscribe(self):
        print('NotifyCharacteristic - onUnsubscribe')

class WriteCharacteristic(Characteristic):

    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': WRITE_CHARACTERISTIC_UUID,
            'properties': ['write'],
            'value': None
        })

        self._value = 0
        self._updateValueCallback = None

    def onWriteRequest(self,data,offset,withoutResponse,callback):
        global android_ID,connectionflag,current_time
        print('WriteCharacteristic - onWriteRequest')
        self._value = data
        android_ID = int(data.decode('utf-8'))
        current_time = time.time()
        connectionflag = True
        callback(Characteristic.RESULT_SUCCESS)
        
def onStateChange(state):
    print('on -> stateChange: ' + state)

    if (state == 'poweredOn'):
        bleno.startAdvertising(NAME, [APPROACH_SERVICE_UUID])
    else:
        bleno.stopAdvertising()


bleno.on('stateChange', onStateChange)

#インスタンスの作成
notifyCharacteristic = NotifyCharacteristic()
writeCharacteristic = WriteCharacteristic()


def onAdvertisingStart(error):
    print('on -> advertisingStart: ' + ('error ' + error if error else 'success'))

    if not error:
        bleno.setServices([
            BlenoPrimaryService({
                'uuid': APPROACH_SERVICE_UUID,
                'characteristics': [
                    notifyCharacteristic,
                    writeCharacteristic
                ]
            })
        ])

def advertise():
    global connection_ID,peripheral_ID
    if notifyCharacteristic._updateValueCallback:
        temp = str(peripheral_ID) +','+ str(connection_ID)
        print('Sending notification with value : ' + str(temp))
        notificationBytes = str(temp).encode()
        notifyCharacteristic._updateValueCallback(notificationBytes)

def getSensors():
    global accel_x,accel_y,accel_z
    sense = SenseHat()
    sense.clear()
    temp_x = [0,0,0,0,0,0,0,0,0,0]
    temp_y = [0,0,0,0,0,0,0,0,0,0]
    temp_z = [0,0,0,0,0,0,0,0,0,0]
    counter = 0
    last_time = 0
    print("getSensors起動")

    while True:
        current_time = round(time.time()*1000)
        if current_time - last_time >= 50:
            last_time = current_time
            acceleration = sense.get_accelerometer_raw()
            temp_x[counter] = acceleration['x']*STANDARD_GRAVITY
            temp_y[counter] = acceleration['y']*STANDARD_GRAVITY
            temp_z[counter] = acceleration['z']*STANDARD_GRAVITY
            # temp_x[counter] = round(acceleration['x']*STANDARD_GRAVITY*100000000)
            # temp_y[counter] = round(acceleration['y']*STANDARD_GRAVITY*100000000)
            # temp_z[counter] = round(acceleration['z']*STANDARD_GRAVITY*100000000)
            counter+=1
            if(counter >= 10):
                accel_x = temp_x
                accel_y = temp_y
                accel_z = temp_z
                counter = 0


def getGPS():
    global lat,lon
    gps_socket = gps3.GPSDSocket()
    data_stream = gps3.DataStream()
    gps_socket.connect()
    gps_socket.watch()
    temp_lat = 0
    temp_lon = 0
    last_lat = 0
    last_lon = 0
    last_time = 0

    print("getGPS起動")
    for new_data in gps_socket:
        if new_data:
            current_time = round(time.time())
            if current_time - last_time >= 0.5:
                last_time = current_time

                data_stream.unpack(new_data)
                temp_lat = data_stream.TPV['lat']
                temp_lon = data_stream.TPV['lon']
                if (temp_lat != 'n/a' and temp_lon != 'n/a'):
                    lat = float(temp_lat)
                    lon = float(temp_lon)
                    # lat = round(float(temp_lat)*10000000)
                    # lon = round(float(temp_lon)*10000000)
                    last_lat = lat
                    last_lon = lon

                else:
                    lat = last_lat
                    lon = last_lon


def registData():
    global peripheral_ID,connection_ID,android_ID,connectionflag,startflag,w3,myContract,lat,lon,accel_x,accel_y,accel_z,datacount
    current_time = 0
    last_time = 0
    executor = ThreadPoolExecutor(max_workers=10)
    while True:
        if connectionflag:
            current_time = round(time.time()*1000)
            if current_time - last_time >=TRANSMISSIOM_TIME:
                last_time = current_time
                if startflag:
                    sendtime = round(time.time()*1000)
                    startflag = False
                    start = myContract.functions.CarStart(peripheral_ID,android_ID,sendtime,connection_ID,lat,lon).transact({'from':w3.eth.accounts[0]})
                    print('Start関数起動:')
                
                tempdata = {} #一回分のデータを格納
                sendtime = round(time.time()*1000)
                tempdata["time"] = sendtime
                tempdata["lat"] = lat
                tempdata["lon"] = lon
                tempdata["accel_x"] = accel_x
                tempdata["accel_y"] = accel_y
                tempdata["accel_z"] = accel_z
                send_data.append(tempdata)
                datacount+=1 
                if (datacount>=chunks):
                    regist = executor.submit(sendData)
                    datacount = 0
        

def Surveillance():
    global current_time,peripheral_ID,android_ID,connectionflag,startflag,w3,myContract,lat,lon
    last_time = 0
    print("Surveillance起動")
    while True:
        if current_time==last_time:
            print("disconnected!")
            notifyCharacteristic._updateValueCallback = None
            connectionflag = False
            startflag = True
            sendtime = round(time.time()*1000)
            finish = myContract.functions.CarFinish(peripheral_ID,sendtime,lat,lon).transact({'from':w3.eth.accounts[0]})
            print('Finish関数起動:')
            sys.exit(1)

        last_time = current_time
        time.sleep(3)

def main_program():
    bleno.on('advertisingStart', onAdvertisingStart)
    bleno.start()
    while True:
        advertise()
        time.sleep(1)


def sendData():
    global URL,peripheral_ID,w3,myContract,lat,lon,accel_x,accel_y,accel_z,send_data
    
    #Swarmへ送信部
    # json_data = json.dumps(send_text).encode("utf-8")
    sendtime = round(time.time()*1000)
    json_data = json.dumps(send_data).encode("utf-8")
    send_data = []
    result = requests.post(URL,json_data,headers={'Content-Type': 'application/json'})
    high = result.text[:32]
    low = result.text[32:]

    #gethへ送信
    regist = myContract.functions.CarRegistData(peripheral_ID,sendtime,high,low).transact({'from':w3.eth.accounts[0]})
    print("regist関数起動")


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(registData())
    #センサーとGPS取得スレッドの作成
    sensorthread = threading.Thread(target=getSensors, args=())
    sensorthread.start()
    gpsthread = threading.Thread(target=getGPS, args=())
    gpsthread.start()

    #ブロックチェーンに登録するスレッドの作成 
    registthread = threading.Thread(target=registData, args=())
    registthread.start() 
    main_program()
