import struct
import requests
import json
import threading
import sys
import os
from web3 import Web3
import time

#ファイルからデータの抽出
f =  open('/Users/sepa/ethereum/truffle/build/contracts/SingleNumRegister.json','r')
# f =  open('/Users/sepa/ethereum/SmartContract/Trial_Swarm//build/contracts/UserContract.json','r')
jsonData = json.load(f)
contract_address = jsonData['networks']['5777']['address']
contract_abi = jsonData['abi']

#ブロックチェーン関係
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
myContract = w3.eth.contract(address=contract_address,abi=contract_abi)
send_high = "333"
send_low = "999"
target = "22c22cb6"


def main_program():
    global URL,peripheral_ID,w3,myContract
    #コマンドライン引数の値の構造体の取得
    # result = myContract.functions.hash_set(send_high,send_low).transact({'from':w3.eth.accounts[1]})

    string = b"\xc6\x9eo\xbd\x05F \x0fZ?/\xe9\xcf\xa3\xd67K#?'\xf9\xfd\xf6\xd1\xee\xb04\xf5\xa45\x9d\x07"

    transaction = w3.eth.getTransaction(string.hex())
    print(transaction)
    # print(transaction.input)
                
if __name__ == '__main__':
    main_program()


