import struct
import requests
import json
import threading
import sys
import os
from web3 import Web3
import time

#ファイルからデータの抽出
# f =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/CarContract.json','r')
f =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/UserContract.json','r')
jsonData = json.load(f)
contract_address = jsonData['networks']['15']['address']
contract_abi = jsonData['abi']
peripheral_ID = 10
ANDROID_ID = 100

#ブロックチェーン関係
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
myContract = w3.eth.contract(address=contract_address,abi=contract_abi)
URL = 'http://127.0.0.1:8500/bzz:/'  #SwarmのURL

def main_program(args):
    global URL,peripheral_ID,w3,myContract
    result = myContract.functions.UserGetData(ANDROID_ID,int(args[1])).call()
    print(result)

if __name__ == '__main__':
    args = sys.argv
    argc = len(args)

    if(argc != 2):
        print("less argument!!")
        sys.exit(1)

    main_program(args)


