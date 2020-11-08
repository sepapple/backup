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
# from scipy import signal
# from pylab import *
# import matplotlib.pyplot as plt

car_file =  open('/Users/sepa/truffle/Trial/build/contracts/CarContract.json','r')
user_file =  open('/Users/sepa/truffle/Trial/build/contracts/UserContract.json','r')
car_jsonData = json.load(car_file)
user_jsonData = json.load(user_file)
car_contract_address = car_jsonData['networks']['15']['address']
user_contract_address = user_jsonData['networks']['15']['address']
car_contract_abi = car_jsonData['abi']
user_contract_abi = user_jsonData['abi']
peripheral_ID = 10
Android_ID = 100
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
car_Contract = w3.eth.contract(address=car_contract_address,abi=car_contract_abi)
user_Contract = w3.eth.contract(address=user_contract_address,abi=user_contract_abi)
fragment_url = 'http://127.0.0.1:8500/bzz:/'  #SwarmのURL
current_time = 0
last_time = 0
pick_range = 60


def GetCarData(args):
    global URL,peripheral_ID,w3,car_Contract,pick_range
    ret_data = []
    temp_data = {}
    transaction_count = 0
    #コマンドライン引数の値の構造体の取得
    result = car_Contract.functions.CarGetData(peripheral_ID,int(args[1])).call()
    #該当範囲探索
    for i in range(result[0][6],int(result[0][7])):
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
                    transaction_count+=1
                    if(transaction_count>=pick_range):
                        return transaction_count
    
    return ret_data


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
    finish_time = time.time()
    print("トランザクションの個数: "+str(pick_range))
    print("抽出時間"+str(finish_time-start_time))
    pick_range+= 60

    start_time = time.time()
    carData =GetCarData(args)
    finish_time = time.time()
    print("トランザクションの個数: "+str(pick_range))
    print("抽出時間"+str(finish_time-start_time))
    pick_range+= 60

    start_time = time.time()
    carData =GetCarData(args)
    finish_time = time.time()
    print("トランザクションの個数: "+str(pick_range))
    print("抽出時間"+str(finish_time-start_time))
    pick_range+= 60

    start_time = time.time()
    carData =GetCarData(args)
    finish_time = time.time()
    print("トランザクションの個数: "+str(pick_range))
    print("抽出時間"+str(finish_time-start_time))
    pick_range+= 60

    start_time = time.time()
    carData =GetCarData(args)
    finish_time = time.time()
    print("トランザクションの個数: "+str(pick_range))
    print("抽出時間"+str(finish_time-start_time))
    # userData = GetUserData(args)
    # DataAnalysis(carData,userData)


