import requests
import re
import binascii

def read():
    target = "0x8e2904e7000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000017543e0a289000000000000000000000000000000000000000000000000000000000000008000000000000000000000000000000000000000000000000000000000000000c00000000000000000000000000000000000000000000000000000000000000020376430653736366535656536373437363034363963373133623066383366666200000000000000000000000000000000000000000000000000000000000000206364386433363135323464313063343265336134363233376634313865326165"
    # result = re.search('17543e0a289',target)
    # result = re.search('a',target)
    # result = re.search('203764306537363665356565363734373630343639633731336230663833666662',target)
    # result = re.search('206364386433363135323464313063343265336134363233376634313865326165',target)
    # string = '206364386433363135323464313063343265336134363233376634313865326165'
    # byte = string.decode('hex')
    # byte = bytearray.fromhex(string).decode()
    # print(byte)
    # print("開始位置: "+ str(result.start()))
    # print("終了位置: "+ str(result.end()))
    # print("切り出した文字列: "+chr(int(target[int(result.start()):int(result.end())])))
    # print(str(int(target[int(result.start())-60:int(result.end())],16)))
    # print("切り出した文字列(10進数): "+str(int(target[int(result.start()):int(result.end())],16)))
    search_target = ['a','17543e0a289','203764306537363665356565363734373630343639633731336230663833666662','206364386433363135323464313063343265336134363233376634313865326165']
    for i in search_target:
        result = re.search(i,target)
        print("開始位置: "+ str(result.start()))
        print("終了位置: "+ str(result.end()))
        print("切り出した文字列: "+str(target[int(result.start()):int(result.end())]))
        print("長さ: "+str(len(str(target[int(result.start()):int(result.end())]))))
        # print(str(int(target[int(result.start())-60:int(result.end())],16)))
        print("切り出した文字列(10進数): "+str(int(target[int(result.start()):int(result.end())],16)))
        print("長さ(10進数): "+str(len(str(int(target[int(result.start()):int(result.end())],16)))))
    # byte = string.decode('hex')
    # byte = bytearray.fromhex(string).decode()

if __name__ == '__main__':
    read()

