import requests

def read():
    # url = 'http://localhost:8500/bzz:/a39f4264fa5f0e0033d734af735927c176a5c7fe303181627411e0de57e01433/'
    # url = 'http://localhost:8500/bzz:/93b6485685e4a6daf2b56b7c76cb5f5ca3c1f91f366a2901c95c915a26836d29/'
    # url = 'http://localhost:8500/bzz:/19bc3a0a08028975686922c05f110b9c465b1a95173f8094ef91b4b5e20778dc/'
    # url = 'http://localhost:8500/bzz:/a8229c93f7941b090e5826154f54a329dc43bf22f66de513f0cfad075f00c8ac/'
    # url = 'http://localhost:8500/bzz:/8d389c62beda62aaba7722b78ca3a6937a75445995af827288c90d83382a4993'
    # url = 'http://localhost:8500/bzz:/0f929707fffe9994b61942f7d838b8a8effff1c664e812dd2353758cadce513c'
    #ラズパイ
    url = 'http://localhost:8500/bzz:/9743aa1c6d1df0798f7024e0680b9beda9b88f3d3c05b3dc8f28fb8f1aef1c33'
    #Android
    url = 'http://localhost:8500/bzz:/f86031c0113388b9e605396f3cbdd364da82bd496f000fbb6dc527c3c8079b27'
    # string = "a8229c93f7941b090e5826154f54a329dc43bf22f66de513f0cfad075f00c8ac"
    # print(len(string))
   
    responce = requests.get(url)
    print(responce.json())
    json_data = responce.json()
    print(str(json_data["time"]))
    print(type(json_data["time"]))

if __name__ == '__main__':
    read()


