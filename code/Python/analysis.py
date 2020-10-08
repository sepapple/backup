import numpy as np
import pandas as pd
import csv
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
#import seaborn as sons

def read():
    # data = pd.read_csv("/Users/sepa/Desktop/Data.csv",header=0)
    # print(data.corr())
    # USERPATH="/Users/sepa/SensorData/UserAllData44.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData46.csv"
    # USERPATH="/Users/sepa/SensorData/UserAllData43.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData44.csv"
    USERPATH="/Users/sepa/SensorData/UserAllData46.csv"
    CARPATH="/Users/sepa/SensorData/CarAllData48.csv"
    userData = []
    carData = []
    dataset = []
    temp = []
    i = 0
    j = 0
    last = 12
    #データの読み込み
    with open(USERPATH) as f:
        for row in csv.reader(f):
            userData.append(row)
    with open(CARPATH) as f:
        for row in csv.reader(f):
            carData.append(row)
    
    userlen = len(userData)
    carlen = len(carData)

    #該当データ検索
    """
    while(i<userlen and j<carlen):
        if(-200<=int(userData[i][0])-int(carData[j][0])<=200):
            for x in range(3,10):
                temp.append(float(userData[i][x]))
                temp.append(float(carData[j][x]))
                dataset.append(temp)
                temp=[]
            i+=1
        elif(int(userData[i][0])-int(carData[j][0])<-200):
            i+=1
        else:
            j+=1
    """
    
    while(i<userlen and i<carlen):
        for x in range(3,10):
            temp.append(float(userData[i][x]))
            temp.append(float(carData[i][x]))
            dataset.append(temp)
            temp=[]
        i+=1
    #生データ
    print(dataset)
    df = pd.DataFrame(dataset,columns=['User','Car'],)
    print(df.corr())

    #正規化
    """
    scaler = MinMaxScaler([-1,1])
    scaler.fit(dataset)
    data_MinMaxScaler = scaler.transform(dataset)
    df = pd.DataFrame(data_MinMaxScaler,columns=['User','Car'],)
    df.describe()
    """
    
    #標準化
    """
    sc = StandardScaler()
    data_std = sc.fit_transform(dataset)
    df = pd.DataFrame(data_std,columns=['User','Car'],)
    print(df.corr())
    """

    # print(df.corr())
    # print(len(dataset))

if __name__ == '__main__':
    read()
