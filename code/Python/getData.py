import requests

def read():
    url = 'http://localhost:8500/bzz:/a8229c93f7941b090e5826154f54a329dc43bf22f66de513f0cfad075f00c8ac/'
    # url = 'http://localhost:8500/bzz:/19bc3a0a08028975686922c05f110b9c465b1a95173f8094ef91b4b5e20778dc/'
    responce = requests.get(url)
    print(responce.text)

if __name__ == '__main__':
    read()


