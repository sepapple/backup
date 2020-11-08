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
car_file =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/CarContract.json','r')
user_file =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/UserContract.json','r')
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
    global URL,peripheral_ID,w3,car_Contract,transaction_count,DataNum
    ret_data = []
    #コマンドライン引数の値の構造体の取得
    result = car_Contract.functions.CarGetData(peripheral_ID,int(args[1])).call()
    #該当範囲探索
    for i in range(result[4],result[5]):
        block = w3.eth.getBlock(i)

        #ブロックの中に入っているトランザクションを抽出
        for addrees in block.transactions:
            transaction = w3.eth.getTransaction(addrees)

            #RegistData関数を対象に抽出
            if(len(transaction.input) == 522):
                # result = re.search(i,target)
                sensor_id = str(int(transaction.input[40:74],16))
                time = str(int(transaction.input[127:138],16))
                high_hex = str(transaction.input[328:394])
                low_hex = str(transaction.input[456:522])
                high = bytearray.fromhex(high_hex).decode()
                low = bytearray.fromhex(low_hex).decode()

                # print("トランザクション内の端末ID: "+sensor_id)
                # print("トランザクション内の時間: "+time)
                # print("前半部分: "+high)
                # print("後半部分: "+low)

                if(sensor_id == '10'):
                    url = fragment_url+high+low
                    url = url.replace(' ','')
                    responce = requests.get(url)
                    # print(responce.json())
                    data = responce.json()
                    ret_data.append(data)
                    transaction_count+=1
                    if(transaction_count >= DataNum):
                        print("抽出したトランザクション量: " + str(transaction_count))
                        return ret_data
    return ret_data


def GetUserData(args):
    global URL,Android_ID,w3,user_Contract,transaction_count,DataNum
    transaction_count = 0
    #コマンドライン引数の値の構造体の取得
    result = user_Contract.functions.UserGetData(Android_ID,int(args[2])).call()
    ret_data = []
    #該当範囲探索
    for i in range(result[4],result[5]):
        block = w3.eth.getBlock(i)

        #ブロックの中に入っているトランザクションを抽出
        for addrees in block.transactions:
            transaction = w3.eth.getTransaction(addrees)

            #RegistData関数を対象に抽出
            if(len(transaction.input) == 522):
                # result = re.search(i,target)
                sensor_id = str(int(transaction.input[40:74],16))
                time = str(int(transaction.input[127:138],16))
                high_hex = str(transaction.input[328:394])
                low_hex = str(transaction.input[456:522])
                high = bytearray.fromhex(high_hex).decode()
                low = bytearray.fromhex(low_hex).decode()

                # print("トランザクション内の端末ID: "+sensor_id)
                # print("トランザクション内の時間: "+time)
                # print("前半部分: "+high)
                # print("後半部分: "+low)

                if(sensor_id == '100'):
                    url = fragment_url+high+low
                    url = url.replace(' ','')
                    responce = requests.get(url)
                    # print(responce.json())
                    data = responce.json()
                    ret_data.append(data)
                    transaction_count+=1
                    if(transaction_count >= DataNum):
                        print("抽出したトランザクション量: " + str(transaction_count))
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
    x_userData = [j for i in userData for j in ast.literal_eval(i['accel_x'])]
    y_userData = [j for i in userData for j in ast.literal_eval(i['accel_y'])]
    z_userData = [j for i in userData for j in ast.literal_eval(i['accel_z'])]

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
    print("--- Swarmからデータ取得---")
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
    carData =GetCarData(args)
    userData = GetUserData(args)
    DataAnalysis(carData,userData)


