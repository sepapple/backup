import requests

def read():
    url = 'http://localhost:8500/bzz:/'
    text_data = "AaBb"
    result = requests.post(url,text_data,headers={'Content-Type': 'text/plain'})
    print(result.text)

if __name__ == '__main__':
    read()


