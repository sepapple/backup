import struct
import requests
import json
import threading
import sys
import os
from web3 import Web3
import time

#ファイルからデータの抽出
f =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/UserContract.json','r')
# f =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/UserContract.json','r')
jsonData = json.load(f)
contract_address = jsonData['networks']['15']['address']
contract_abi = jsonData['abi']
peripheral_ID = 10
Android_ID = 100

#ブロックチェーン関係
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
myContract = w3.eth.contract(address=contract_address,abi=contract_abi)
fragment_url = 'http://127.0.0.1:8500/bzz:/'  #SwarmのURL

def main_program(args):
    global URL,peripheral_ID,w3,myContract
    #コマンドライン引数の値の構造体の取得
    result = myContract.functions.UserGetData(Android_ID,int(args[1])).call()
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

                if(sensor_id == '100'):
                    url = fragment_url+high+low
                    url = url.replace(' ','')
                    responce = requests.get(url)
                    print(responce.json())
                    # print("トランザクション内の端末ID: "+sensor_id)
                    # print("トランザクション内の時間: "+time)
                    # print("前半部分: "+high)
                    # print("後半部分: "+low)
                    # data = responce.json()
                    # print(data['time'])        
                    # print(data['accel_x'])        

                    # print(data[accel_x])




if __name__ == '__main__':
    args = sys.argv
    argc = len(args)

    if(argc != 2):
        print("less argument!!")
        sys.exit(1)

    main_program(args)


