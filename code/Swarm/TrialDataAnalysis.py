#第一引数にCarStructの番号,第二引数にUserStructの番号
#3-8,4-9,5-10
import struct
import requests
import json
import threading
import sys
import os
from web3 import Web3
import time
import ast
import numpy as np
import pandas as pd
import csv
from scipy import signal
from pylab import *
import matplotlib.pyplot as plt


#ファイルからデータの抽出
car_file =  open('/Users/sepa/truffle/Trial/build/contracts/CarContract.json','r')
user_file =  open('/Users/sepa/truffle/Trial/build/contracts/UserContract.json','r')
# f =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/UserContract.json','r')
car_jsonData = json.load(car_file)
user_jsonData = json.load(user_file)
car_contract_address = car_jsonData['networks']['15']['address']
user_contract_address = user_jsonData['networks']['15']['address']
car_contract_abi = car_jsonData['abi']
user_contract_abi = user_jsonData['abi']
peripheral_ID = 10
Android_ID = 100
start_time = 0
finish_time = 0
transaction_count = 0
DataNum = 300

#ブロックチェーン関係
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
car_Contract = w3.eth.contract(address=car_contract_address,abi=car_contract_abi)
user_Contract = w3.eth.contract(address=user_contract_address,abi=user_contract_abi)
fragment_url = 'http://127.0.0.1:8500/bzz:/'  #SwarmのURL


def GetCarData(args):
    global URL,peripheral_ID,w3,car_Contract,transaction_count,DataNum,carData
    ret_data = []
    temp_data = {}
    counter = 0
    #コマンドライン引数の値の構造体の取得
    result = car_Contract.functions.CarGetData(peripheral_ID,int(args[1])).call()
    #該当範囲探索
    for i in range(result[0][6],int(result[0][6])+DataNum):
        block = w3.eth.getBlock(i)

        #ブロックの中に入っているトランザクションを抽出
        for addrees in block.transactions:
            transaction = w3.eth.getTransaction(addrees)

            #RegistData関数を対象に抽出
            if(len(transaction.input) == 2570):
                # result = re.search(i,target)
                sensor_id = str(int(transaction.input[40:74],16))

                if(sensor_id == '10'):
                    accel_x = []
                    accel_y = []
                    accel_z = []
                    temp_data = {}
                    counter += 1
                    time = str(int(transaction.input[127:138],16))
                    lat = int.from_bytes(bytearray.fromhex(transaction.input[194:202]),byteorder='big')
                    lon = int.from_bytes(bytearray.fromhex(transaction.input[258:266]),byteorder='big')
                    accel_x1 = int.from_bytes(bytearray.fromhex(transaction.input[578:586]),byteorder='big',signed=True)/100000000 
                    accel_x2 = int.from_bytes(bytearray.fromhex(transaction.input[642:650]),byteorder='big',signed=True)/100000000
                    accel_x3 = int.from_bytes(bytearray.fromhex(transaction.input[706:714]),byteorder='big',signed=True)/100000000
                    accel_x4 = int.from_bytes(bytearray.fromhex(transaction.input[770:778]),byteorder='big',signed=True)/100000000
                    accel_x5 = int.from_bytes(bytearray.fromhex(transaction.input[834:842]),byteorder='big',signed=True)/100000000
                    accel_x6 = int.from_bytes(bytearray.fromhex(transaction.input[898:902]),byteorder='big',signed=True)/100000000
                    accel_x7 = int.from_bytes(bytearray.fromhex(transaction.input[962:970]),byteorder='big',signed=True)/100000000
                    accel_x8 = int.from_bytes(bytearray.fromhex(transaction.input[1026:1034]),byteorder='big',signed=True)/100000000
                    accel_x9 = int.from_bytes(bytearray.fromhex(transaction.input[1090:1098]),byteorder='big',signed=True)/100000000
                    accel_x10= int.from_bytes(bytearray.fromhex(transaction.input[1154:1162]),byteorder='big',signed=True)/100000000
                    accel_y1 = int.from_bytes(bytearray.fromhex(transaction.input[1282:1290]),byteorder='big',signed=True)/100000000
                    accel_y2 = int.from_bytes(bytearray.fromhex(transaction.input[1346:1354]),byteorder='big',signed=True)/100000000
                    accel_y3 = int.from_bytes(bytearray.fromhex(transaction.input[1410:1418]),byteorder='big',signed=True)/100000000
                    accel_y4 = int.from_bytes(bytearray.fromhex(transaction.input[1474:1482]),byteorder='big',signed=True)/100000000
                    accel_y5 = int.from_bytes(bytearray.fromhex(transaction.input[1538:1546]),byteorder='big',signed=True)/100000000
                    accel_y6 = int.from_bytes(bytearray.fromhex(transaction.input[1602:1610]),byteorder='big',signed=True)/100000000
                    accel_y7 = int.from_bytes(bytearray.fromhex(transaction.input[1666:1674]),byteorder='big',signed=True)/100000000
                    accel_y8 = int.from_bytes(bytearray.fromhex(transaction.input[1730:1738]),byteorder='big',signed=True)/100000000
                    accel_y9 = int.from_bytes(bytearray.fromhex(transaction.input[1794:1802]),byteorder='big',signed=True)/100000000
                    accel_y10 = int.from_bytes(bytearray.fromhex(transaction.input[1858:1866]),byteorder='big',signed=True)/100000000
                    accel_z1 = int.from_bytes(bytearray.fromhex(transaction.input[1986:1994]),byteorder='big',signed=True)/100000000
                    accel_z2 = int.from_bytes(bytearray.fromhex(transaction.input[2050:2058]),byteorder='big',signed=True)/100000000
                    accel_z3 = int.from_bytes(bytearray.fromhex(transaction.input[2114:2122]),byteorder='big',signed=True)/100000000
                    accel_z4 = int.from_bytes(bytearray.fromhex(transaction.input[2178:2186]),byteorder='big',signed=True)/100000000
                    accel_z5 = int.from_bytes(bytearray.fromhex(transaction.input[2242:2250]),byteorder='big',signed=True)/100000000
                    accel_z6 = int.from_bytes(bytearray.fromhex(transaction.input[2306:2314]),byteorder='big',signed=True)/100000000
                    accel_z7 = int.from_bytes(bytearray.fromhex(transaction.input[2370:2378]),byteorder='big',signed=True)/100000000
                    accel_z8 = int.from_bytes(bytearray.fromhex(transaction.input[2434:2442]),byteorder='big',signed=True)/100000000
                    accel_z9 = int.from_bytes(bytearray.fromhex(transaction.input[2498:2506]),byteorder='big',signed=True)/100000000
                    accel_z10 = int.from_bytes(bytearray.fromhex(transaction.input[2562:2570]),byteorder='big',signed=True)/100000000
                    accel_x.append(accel_x1)
                    accel_x.append(accel_x2)
                    accel_x.append(accel_x3)
                    accel_x.append(accel_x4)
                    accel_x.append(accel_x5)
                    accel_x.append(accel_x6)
                    accel_x.append(accel_x7)
                    accel_x.append(accel_x8)
                    accel_x.append(accel_x9)
                    accel_x.append(accel_x10)
                    accel_y.append(accel_y1)
                    accel_y.append(accel_y2)
                    accel_y.append(accel_y3)
                    accel_y.append(accel_y4)
                    accel_y.append(accel_y5)
                    accel_y.append(accel_y6)
                    accel_y.append(accel_y7)
                    accel_y.append(accel_y8)
                    accel_y.append(accel_y9)
                    accel_y.append(accel_y10)
                    accel_z.append(accel_z1)
                    accel_z.append(accel_z2)
                    accel_z.append(accel_z3)
                    accel_z.append(accel_z4)
                    accel_z.append(accel_z5)
                    accel_z.append(accel_z6)
                    accel_z.append(accel_z7)
                    accel_z.append(accel_z8)
                    accel_z.append(accel_z9)
                    accel_z.append(accel_z10)
                    temp_data['time'] = time
                    temp_data['lat'] = lat
                    temp_data['lon'] = lon
                    temp_data['accel_x'] = accel_x
                    temp_data['accel_y'] = accel_y
                    temp_data['accel_z'] = accel_z
                    ret_data.append(temp_data)
                    if(counter >= DataNum):
                        print("車側トランザクション量: " + str(counter))
                        return ret_data
    
    return ret_data


def GetUserData(args):
    global URL,Android_ID,w3,user_Contract,transaction_count,DataNum
    transaction_count = 0
    #コマンドライン引数の値の構造体の取得
    result = user_Contract.functions.UserGetData(Android_ID,int(args[2])).call()
    ret_data = []
    temp_data = {}
    counter = 0
    #該当範囲探索
    for i in range(result[0][6],int(result[0][6])+DataNum):
        block = w3.eth.getBlock(i)

        #ブロックの中に入っているトランザクションを抽出
        for addrees in block.transactions:
            transaction = w3.eth.getTransaction(addrees)

            #RegistData関数を対象に抽出
            if(len(transaction.input) == 2570):
                # result = re.search(i,target)
                sensor_id = str(int(transaction.input[40:74],16))

                if(sensor_id == '100'):
                    accel_x = []
                    accel_y = []
                    accel_z = []
                    temp_data = {}
                    counter += 1
                    time = str(int(transaction.input[127:138],16))
                    lat = int.from_bytes(bytearray.fromhex(transaction.input[194:202]),byteorder='big')
                    lon = int.from_bytes(bytearray.fromhex(transaction.input[258:266]),byteorder='big')
                    accel_x1 = int.from_bytes(bytearray.fromhex(transaction.input[578:586]),byteorder='big',signed=True)/100000000 
                    accel_x2 = int.from_bytes(bytearray.fromhex(transaction.input[642:650]),byteorder='big',signed=True)/100000000
                    accel_x3 = int.from_bytes(bytearray.fromhex(transaction.input[706:714]),byteorder='big',signed=True)/100000000
                    accel_x4 = int.from_bytes(bytearray.fromhex(transaction.input[770:778]),byteorder='big',signed=True)/100000000
                    accel_x5 = int.from_bytes(bytearray.fromhex(transaction.input[834:842]),byteorder='big',signed=True)/100000000
                    accel_x6 = int.from_bytes(bytearray.fromhex(transaction.input[898:902]),byteorder='big',signed=True)/100000000
                    accel_x7 = int.from_bytes(bytearray.fromhex(transaction.input[962:970]),byteorder='big',signed=True)/100000000
                    accel_x8 = int.from_bytes(bytearray.fromhex(transaction.input[1026:1034]),byteorder='big',signed=True)/100000000
                    accel_x9 = int.from_bytes(bytearray.fromhex(transaction.input[1090:1098]),byteorder='big',signed=True)/100000000
                    accel_x10= int.from_bytes(bytearray.fromhex(transaction.input[1154:1162]),byteorder='big',signed=True)/100000000
                    accel_y1 = int.from_bytes(bytearray.fromhex(transaction.input[1282:1290]),byteorder='big',signed=True)/100000000
                    accel_y2 = int.from_bytes(bytearray.fromhex(transaction.input[1346:1354]),byteorder='big',signed=True)/100000000
                    accel_y3 = int.from_bytes(bytearray.fromhex(transaction.input[1410:1418]),byteorder='big',signed=True)/100000000
                    accel_y4 = int.from_bytes(bytearray.fromhex(transaction.input[1474:1482]),byteorder='big',signed=True)/100000000
                    accel_y5 = int.from_bytes(bytearray.fromhex(transaction.input[1538:1546]),byteorder='big',signed=True)/100000000
                    accel_y6 = int.from_bytes(bytearray.fromhex(transaction.input[1602:1610]),byteorder='big',signed=True)/100000000
                    accel_y7 = int.from_bytes(bytearray.fromhex(transaction.input[1666:1674]),byteorder='big',signed=True)/100000000
                    accel_y8 = int.from_bytes(bytearray.fromhex(transaction.input[1730:1738]),byteorder='big',signed=True)/100000000
                    accel_y9 = int.from_bytes(bytearray.fromhex(transaction.input[1794:1802]),byteorder='big',signed=True)/100000000
                    accel_y10 = int.from_bytes(bytearray.fromhex(transaction.input[1858:1866]),byteorder='big',signed=True)/100000000
                    accel_z1 = int.from_bytes(bytearray.fromhex(transaction.input[1986:1994]),byteorder='big',signed=True)/100000000
                    accel_z2 = int.from_bytes(bytearray.fromhex(transaction.input[2050:2058]),byteorder='big',signed=True)/100000000
                    accel_z3 = int.from_bytes(bytearray.fromhex(transaction.input[2114:2122]),byteorder='big',signed=True)/100000000
                    accel_z4 = int.from_bytes(bytearray.fromhex(transaction.input[2178:2186]),byteorder='big',signed=True)/100000000
                    accel_z5 = int.from_bytes(bytearray.fromhex(transaction.input[2242:2250]),byteorder='big',signed=True)/100000000
                    accel_z6 = int.from_bytes(bytearray.fromhex(transaction.input[2306:2314]),byteorder='big',signed=True)/100000000
                    accel_z7 = int.from_bytes(bytearray.fromhex(transaction.input[2370:2378]),byteorder='big',signed=True)/100000000
                    accel_z8 = int.from_bytes(bytearray.fromhex(transaction.input[2434:2442]),byteorder='big',signed=True)/100000000
                    accel_z9 = int.from_bytes(bytearray.fromhex(transaction.input[2498:2506]),byteorder='big',signed=True)/100000000
                    accel_z10 = int.from_bytes(bytearray.fromhex(transaction.input[2562:2570]),byteorder='big',signed=True)/100000000
                    accel_x.append(accel_x1)
                    accel_x.append(accel_x2)
                    accel_x.append(accel_x3)
                    accel_x.append(accel_x4)
                    accel_x.append(accel_x5)
                    accel_x.append(accel_x6)
                    accel_x.append(accel_x7)
                    accel_x.append(accel_x8)
                    accel_x.append(accel_x9)
                    accel_x.append(accel_x10)
                    accel_y.append(accel_y1)
                    accel_y.append(accel_y2)
                    accel_y.append(accel_y3)
                    accel_y.append(accel_y4)
                    accel_y.append(accel_y5)
                    accel_y.append(accel_y6)
                    accel_y.append(accel_y7)
                    accel_y.append(accel_y8)
                    accel_y.append(accel_y9)
                    accel_y.append(accel_y10)
                    accel_z.append(accel_z1)
                    accel_z.append(accel_z2)
                    accel_z.append(accel_z3)
                    accel_z.append(accel_z4)
                    accel_z.append(accel_z5)
                    accel_z.append(accel_z6)
                    accel_z.append(accel_z7)
                    accel_z.append(accel_z8)
                    accel_z.append(accel_z9)
                    accel_z.append(accel_z10)
                    temp_data['time'] = time
                    temp_data['lat'] = lat
                    temp_data['lon'] = lon
                    temp_data['accel_x'] = accel_x
                    temp_data['accel_y'] = accel_y
                    temp_data['accel_z'] = accel_z
                    ret_data.append(temp_data)

                    if(counter >= DataNum):
                        print("ユーザ側トランザクション量: " + str(counter))
                        return ret_data
    return ret_data


def DataAnalysis(carData,userData):
    global start_time
    user_synthetic = []
    car_synthetic = []
    dataset_normalization = []
    dataset_moving = []
    temp = []
    start = 0
    window = 10
    i=0
    order = 5
    list_window = 20
    biggest_corr_normalization = 0

    # x_userData = [j for j in i['accel_x'] for i in userData]
    x_userData = [j for i in userData for j in i['accel_x']]
    y_userData = [j for i in userData for j in i['accel_y']]
    z_userData = [j for i in userData for j in i['accel_z']]

    x_carData = [j for i in carData for j in i['accel_x']]
    y_carData = [j for i in carData for j in i['accel_y']]
    z_carData = [j for i in carData for j in i['accel_z']]

    #合成加速度
    user_synthetic = [np.sqrt(x_userData[i]**(2)+y_userData[i]**(2)+z_userData[i]**(2)) for i in range(0,len(x_userData))]
    car_synthetic = [np.sqrt(x_carData[i]**(2)+y_carData[i]**(2)+z_carData[i]**(2)) for i in range(0,len(x_carData))]
    # print("スマホのデータ量: "+str(len(user_synthetic)))
    # print("ラズパイのデータ量: "+str(len(car_synthetic)))
    #正規化
    if (abs(np.max(user_synthetic)) >= abs(np.min(user_synthetic))):
            user_normalization = [y / np.max(user_synthetic) for y in user_synthetic]
    else:
            user_normalization = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

    if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
            car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
    else:
            car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]

    while(i<len(user_normalization) and i<len(car_normalization)):
        temp.append(float(user_normalization[i]))
        temp.append(float(car_normalization[i]))
        dataset_normalization.append(temp)
        temp=[]
        i+=1


    # print(user_normalization)
    df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
    # print("正規化後の相関係数")
    # print(df_normalization.corr())
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')

    # maxid = signal.argrelmax(user_ave,order=10)
    # minid = signal.argrelmin(car_ave,order=10)

    user_max = signal.argrelmax(np.array(user_normalization),order = order)
    car_max = signal.argrelmax(np.array(car_normalization),order = order)
    # minid = signal.argrelmin(np.array(car_normalization),order=10)


    # print(user_max)
    # print(minid)
    user_x = np.array([i for i in range(len(user_max[0]))])
    # x = np.array([i for i in range(start, start+len(user_max))])
    # x = np.array([i for i in range(start, start+len(user_normalization))])
    # y = np.array([user_normalization[i] for i in user_max.tolist()])    
    # y = np.array(user_normalization)    
    user_y = []
    for i in range(len(user_max[0])):
        user_y.append(user_normalization[user_max[0][i]])
    
    
    #移動平均を取得
    v = np.ones(window)/window
    user_ave = np.convolve(user_y,v,mode='same')
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    ax1.plot(range(0,len(user_normalization)), user_normalization[0:len(user_normalization)],color='b',label='UserData') 
    ax1.set_xlim([0,len(user_normalization)]) 
    ax1.set_ylim([-1.0, 1.0]) 
    ax1.set_xlabel("count ",size=10)
    ax1.set_ylabel("user synthetic accel",size=10)
    
    ax2.plot(range(0,len(car_normalization)), car_normalization[0:len(car_normalization)],color='b',label='carData') 
    ax2.set_xlim([0,len(car_normalization)]) 
    ax2.set_ylim([-1.0, 1.0]) 
    ax2.set_xlabel("count ",size=10)
    ax2.set_ylabel("car synthetic accel",size=10)
    
    # user_y = np.array(user_y)
    user_x = [i for i in range(len(user_ave))]
    # ax3.plot(range(start, start+len(user_ave)), user_ave[start:start+len(user_ave)],label='UserData') 
    # ax3.plot(x, user_normalization[start:start+len(user_normalization)],label='UserData') 
    ax3.plot(user_x,user_ave,color='b',label='UserData') 
    # ax3.plot(x[maxid],y[maxid],'ro',label='ピーク値')
    # ax3.plot(x[minid],y[minid],'bo',label='ピーク値(最小)')
    # ax3.set_xlim([start,start+len(user_normalization)]) 
    ax3.set_xlim([start,start+len(user_y)]) 
    ax3.set_ylim([-1.0, 1.0]) 
    # ax3.plot(x[maxid],
    ax3.set_xlabel("count ",size=10)
    ax3.set_ylabel("synthetic accel",size=10)
    ax3.legend()

    car_x = np.array([i for i in range(len(car_max[0]))])
    car_y = []
    for i in range(len(car_max[0])):
        car_y.append(car_normalization[car_max[0][i]])

    #移動平均
    
    car_ave = np.convolve(car_y,v,mode='same')
    car_x = [i for i in range(len(car_ave))]

    ax4.plot(car_x,car_ave,color='r',label='CarData') 
    ax4.set_xlim([start,start+len(car_y)]) 
    ax4.set_ylim([-1.0, 1.0]) 
    ax4.legend()

    for slide in range(list_window):
        i=0
        dataset_normalization = []
        while(i<len(user_ave) and i<len(car_ave)):
            temp.append(user_ave[i])
            temp.append(car_ave[i])
            dataset_normalization.append(temp)
            temp=[]
            i+=1
    
        df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
        print("User側移動平均後の相関係数スライド数: "+ str(slide+1))
        print(df_normalization.corr())
        user_ave = np.delete(user_ave,0)
        # user_ave.pop(0)     
        if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
            biggest_corr_normalization = df_normalization.corr().iat[0,1]


    user_ave = np.convolve(user_y,v,mode='same')

    for slide in range(list_window):
        i=0
        dataset_normalization = []
        while(i<len(user_ave) and i<len(car_ave)):
            temp.append(user_ave[i])
            temp.append(car_ave[i])
            dataset_normalization.append(temp)
            temp=[]
            i+=1
    
        df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
        print("Car側移動平均後の相関係数スライド数: "+ str(slide+1))
        print(df_normalization.corr())
        car_ave = np.delete(car_ave,0)
        # car_y.pop(0)     

        if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
            biggest_corr_normalization = df_normalization.corr().iat[0,1]
    finish_time = time.time()
    print("移動平均の最大相関係数: " + str(biggest_corr_normalization))
    print("---ブロックチェーンから直接取得---")
    print("データ取得から解析までの時間: "+ str(finish_time-start_time))
    plt.show()


if __name__ == '__main__':
    args = sys.argv
    argc = len(args)

    if(argc < 3):
        print("too less argument!")
        sys.exit(1)
    elif (argc > 3):
        print("too many argument!")
        sys.exit(1)
    start_time = time.time()
    carData = GetCarData(args)
    userData = GetUserData(args)
    DataAnalysis(carData,userData)

