import struct
import requests
import json
import threading
import sys
import os
from web3 import Web3
import time



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
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
car_Contract = w3.eth.contract(address=car_contract_address,abi=car_contract_abi)
user_Contract = w3.eth.contract(address=user_contract_address,abi=user_contract_abi)
fragment_url = 'http://127.0.0.1:8500/bzz:/'  #SwarmのURL
current_time = 0
last_time = 0


def CarGas(args):
    global URL,peripheral_ID,w3,car_Contract,current_time,last_time
    #コマンドライン引数の値の構造体の取得
    counter = 0
    total = 0

    result = car_Contract.functions.CarGetData(peripheral_ID,int(args[1])).call()
    #該当範囲探索
    for i in range(result[0][6],result[0][7]):
        block = w3.eth.getBlock(i)

        #ブロックの中に入っているトランザクションを抽出
        for addrees in block.transactions:
            transaction = w3.eth.getTransaction(addrees)

            #RegistData関数を対象に抽出
            if(len(transaction.input) == 2570):
                # result = re.search(i,target)
                sensor_id = str(int(transaction.input[40:74],16))
                time = str(int(transaction.input[127:138],16))
                # high_hex = str(transaction.input[328:394])
                # low_hex = str(transaction.input[456:522])
                # high = bytearray.fromhex(high_hex).decode()
                # low = bytearray.fromhex(low_hex).decode()

                # print("トランザクション内の端末ID: "+sensor_id)
                # print("トランザクション内の時間: "+time)
                # print("前半部分: "+high)
                # print("後半部分: "+low)
                
                if(sensor_id == '10'):
                    total += int(transaction.gas)
                    # current_time = int(time)
                    # print(current_time-last_time)
                    # last_time = current_time
                    # print("Gas値: "+ str(transaction.gas))
                    # print("Gas値: "+ str(transaction))
                    counter+=1
        
    print("----Car----")
    print("Gas合計値: "+ str(total))
    print("全トランザクション: "+ str(counter))
    print("平均: "+ str(int(total/counter)))

def UserGas(args):
    global URL,Android_ID,w3,user_Contract,current_time,last_time
    #コマンドライン引数の値の構造体の取得
    counter = 0
    total = 0
    current_time = 0
    last_time = 0

    result = user_Contract.functions.UserGetData(Android_ID,int(args[2])).call()
    #該当範囲探索
    for i in range(result[0][6],result[0][7]):
        block = w3.eth.getBlock(i)

        #ブロックの中に入っているトランザクションを抽出
        for addrees in block.transactions:
            transaction = w3.eth.getTransaction(addrees)

            #RegistData関数を対象に抽出
            if(len(transaction.input) == 2570):
                # result = re.search(i,target)
                sensor_id = str(int(transaction.input[40:74],16))
                # time = str(int(transaction.input[127:138],16))
                # high_hex = str(transaction.input[328:394])
                # low_hex = str(transaction.input[456:522])
                # high = bytearray.fromhex(high_hex).decode()
                # low = bytearray.fromhex(low_hex).decode()

                # print("トランザクション内の端末ID: "+sensor_id)
                # print("トランザクション内の時間: "+time)
                # print("前半部分: "+high)
                # print("後半部分: "+low)

                if(sensor_id == '100'):
                    total += int(transaction.gas)
                    # current_time = int(time)
                    # print(current_time-last_time)
                    # last_time = current_time
                    # print("Gas値: "+ str(transaction.gas))
                    counter+=1
        
    print('\n'+"----User----")
    print("Gas合計値: "+ str(total))
    print("全トランザクション: "+ str(counter))
    print("平均: "+ str(int(total/counter)))

                
if __name__ == '__main__':
    args = sys.argv
    argc = len(args)

    if(argc < 3):
        print("too less argument!")
        sys.exit(1)
    elif (argc > 3):
        print("too many argument!")
        sys.exit(1)

    CarGas(args)
    UserGas(args)
