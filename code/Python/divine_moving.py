import numpy as np
import pandas as pd
import csv
from scipy import signal
from pylab import *
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#import seaborn as sons

def read():
    # data = pd.read_csv("/Users/sepa/Desktop/Data.csv",header=0)
    # print(data.corr())
    # USERPATH="/Users/sepa/SensorData/XYZUserData42.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData40.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData44.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData46.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData45.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData47.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData46.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData48.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData47.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData49.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData48.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData50.csv"

    # USERPATH="/Users/sepa/SensorData/XYZUserData52.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData58.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData53.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData60.csv"

    #低い値
    # USERPATH="/Users/sepa/SensorData/XYZUserData54.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData61.csv"

    # USERPATH="/Users/sepa/SensorData/XYZUserData55.csv" #1
    # CARPATH="/Users/sepa/SensorData/XYZCarData62.csv" #4
    # USERPATH="/Users/sepa/SensorData/XYZUserData56.csv" #2
    # CARPATH="/Users/sepa/SensorData/XYZCarData63.csv" #3
    # USERPATH="/Users/sepa/SensorData/XYZUserData57.csv" #3
    # CARPATH="/Users/sepa/SensorData/XYZCarData64.csv" #2
    USERPATH="/Users/sepa/SensorData/XYZUserData58.csv" #4
    # CARPATH="/Users/sepa/SensorData/XYZCarData65.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData59.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData66.csv" #1
    userData = []
    carData = []
    user_synthetic = []
    car_synthetic = []
    dataset_normalization = []
    dataset_moving = []
    temp = []
    start = 0
    i=0
    order = 5
    list_window = 20
    biggest_corr_normalization = 0
    #データの読み込み
    userDF = pd.read_csv(USERPATH,header=0)
    carDF = pd.read_csv(CARPATH,header=0)
    #データ抽出
    x_userData = userDF.iloc[:, 3:13].values.flatten()
    y_userData = userDF.iloc[:, 13:23].values.flatten()
    z_userData = userDF.iloc[:, 23:33].values.flatten()
    
    x_carData = carDF.iloc[:, 3:13].values.flatten()
    y_carData = carDF.iloc[:, 13:23].values.flatten()
    z_carData = carDF.iloc[:, 23:33].values.flatten()
    #合成加速度
    user_synthetic = [np.sqrt(x_userData[i]**(2)+y_userData[i]**(2)+z_userData[i]**(2)) for i in range(0,len(x_userData))]
    car_synthetic = [np.sqrt(x_carData[i]**(2)+y_carData[i]**(2)+z_carData[i]**(2)) for i in range(0,len(x_carData))]
    # print(synthetic)
    
    #正規化
    if (abs(np.max(user_synthetic)) >= abs(np.min(user_synthetic))):
            user = [y / np.max(user_synthetic) for y in user_synthetic]
    else:
            user = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

    if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
            car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
    else:
            car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]

    window = 10
    #移動平均を取得
    v = np.ones(window)/window
    user_normalization = np.convolve(user,v,mode='same')
    car_normalization = np.convolve(car_normalization,v,mode='same')
    slide_width = 10
    for slide in range(slide_width):
        dataset_normalization = []
        while(i<len(user_normalization) and i<len(car_normalization)):
            temp.append(float(user_normalization[i]))
            temp.append(float(car_normalization[i]))
            dataset_normalization.append(temp)
            temp=[]
            i+=1


        counter = 0
        num = 20
        for i in range(int(len(dataset_normalization)/num)):
            analysis = [dataset_normalization[i*num+j] for j in range(num)]    
            df_normalization = pd.DataFrame(analysis,columns=['User','Car'],)
            # print(str(i)+"回目相関係数: "+ str(df_normalization.corr().iat[0,1]))
            if(abs(df_normalization.corr().iat[0,1])>=0.7):
                counter+=1
        
        print(str(int(len(dataset_normalization)/num))+"回中条件を超えた回数(乗客側): "+str(counter))
        counter = 0
        user_normalization = np.delete(user_normalization,0)

    user_normalization = np.convolve(user,v,mode='same')

    for slide in range(slide_width):
        dataset_normalization = []
        while(i<len(user_normalization) and i<len(car_normalization)):
            temp.append(float(user_normalization[i]))
            temp.append(float(car_normalization[i]))
            dataset_normalization.append(temp)
            temp=[]
            i+=1


        counter = 0
        num = 20
        for i in range(int(len(dataset_normalization)/num)):
            analysis = [dataset_normalization[i*num+j] for j in range(num)]    
            df_normalization = pd.DataFrame(analysis,columns=['User','Car'],)
            # print(str(i)+"回目相関係数: "+ str(df_normalization.corr().iat[0,1]))
            if(abs(df_normalization.corr().iat[0,1])>=0.7):
                counter+=1
        
        print(str(int(len(dataset_normalization)/num))+"回中条件を超えた回数(車側): "+str(counter))
        counter = 0
        car_normalization = np.delete(car_normalization,0)

if __name__ == '__main__':
    read()
