import numpy as np
import pandas as pd
import csv
from scipy import signal
from pylab import *
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#import seaborn as sons

def user_read():
    # data = pd.read_csv("/Users/sepa/Desktop/Data.csv",header=0)
    # print(data.corr())
    # USERPATH="/Users/sepa/SensorData/XYZUserData42.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData40.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData44.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData46.csv"
    #一番良く出るデータ
    # USERPATH="/Users/sepa/SensorData/XYZUserData45.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData47.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData46.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData48.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData47.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData49.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData48.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData50.csv"
    USERPATH="/Users/sepa/SensorData/XYZUserData52.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData58.csv"
    list_window = 20 
    userData = []
    carData = []
    user_normalization =[]
    car_normalization =[]
    user_synthetic = []
    car_synthetic = []
    dataset_normalization = []
    dataset_moving = []
    temp = []
    start = 0
    window = 10
    i=0
    biggest_corr_normalization = 0
    biggest_corr_moving = 0
    flag = False
    counter = 0

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

    #z軸加速度
    # user_synthetic = [z_userData[i] for i in range(0,len(z_userData))]
    # car_synthetic = [z_carData[i] for i in range(0,len(z_carData))]


    for slide in range(list_window):
        #スライド
        if (abs(np.max(user_synthetic)) >= abs(np.min(user_synthetic))):
                user_normalization = [y / np.max(user_synthetic) for y in user_synthetic]
        else:
                user_normalization = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

        if(flag == False):
            if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
                    car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
            else:
                    car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]
    

        flag = True
        dataset_normalization = []
        i=0
        while(i<len(user_normalization) and i<len(car_normalization)):
            temp.append(float(user_normalization[i]))
            temp.append(float(car_normalization[i]))
            dataset_normalization.append(temp)
            temp=[]
            i+=1
        
        # print(dataset_normalization)

        # print("dataset:1番目の値"+str(dataset_normalization[0]))

        df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
        print("User側正規化後の相関係数スライド数: "+ str(slide+1))
        print(df_normalization.corr())
        
        if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
            biggest_corr_normalization = df_normalization.corr().iat[0,1]

        v = np.ones(window)/window
        user_ave = np.convolve(user_normalization,v,mode='same')
        car_ave = np.convolve(car_normalization,v,mode='same')
        i=0
        dataset_moving = []

        while(i<len(user_ave) and i<len(car_ave)):
            temp.append(float(user_ave[i]))
            temp.append(float(car_ave[i]))
            dataset_moving.append(temp)
            temp=[]
            i+=1

        # print("dataset:1番目の値"+str(dataset_moving[0]))

        df_moving = pd.DataFrame(dataset_moving,columns=['User','Car'],)
        print("User側移動平均の相関係数スライド数: "+ str(slide+1))
        print(df_moving.corr())
        if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
            biggest_corr_moving = df_moving.corr().iat[0,1]
        
        user_synthetic.pop(0)
        counter+=1
        print("normalizationlength: "+ str(len(dataset_normalization)))
        print("movinglength: "+ str(len(dataset_moving)))
    
    user_synthetic = [np.sqrt(x_userData[i]**(2)+y_userData[i]**(2)+z_userData[i]**(2)) for i in range(0,len(x_userData))]

    for slide in range(list_window):
        #スライド
        if(flag == False):
            if (abs(np.max(user_synthetic)) >= abs(np.min(user_synthetic))):
                    user_normalization = [y / np.max(user_synthetic) for y in user_synthetic]
            else:
                    user_normalization = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

        if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
                car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
        else:
                car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]
        #正規化
        
        #データセット作り
        flag = True
        dataset_normalization = []
        i=0
        while(i<len(user_normalization) and i<len(car_normalization)):
            temp.append(float(user_normalization[i]))
            temp.append(float(car_normalization[i]))
            dataset_normalization.append(temp)
            temp=[]
            i+=1

        
        df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
        print("Car側正規化後の相関係数スライド数: "+ str(slide+1))
        print(df_normalization.corr())
        
        if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
            biggest_corr_normalization = df_normalization.corr().iat[0,1]

        v = np.ones(window)/window
        user_ave = np.convolve(user_normalization,v,mode='same')
        car_ave = np.convolve(car_normalization,v,mode='same')
        i=0
        dataset_moving = []
        while(i<len(user_ave) and i<len(car_ave)):
            temp.append(float(user_ave[i]))
            temp.append(float(car_ave[i]))
            dataset_moving.append(temp)
            temp=[]
            i+=1
        print("normalizationlength: "+ str(len(dataset_normalization)))
        print("movinglength: "+ str(len(dataset_moving)))
        df_moving = pd.DataFrame(dataset_moving,columns=['User','Car'],)
        print("Car側移動平均の相関係数スライド数: "+ str(slide+1))
        print(df_moving.corr())


        if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
            biggest_corr_moving = df_moving.corr().iat[0,1]

        car_synthetic.pop(0)

    print("正規化の最大相関係数: " + str(biggest_corr_normalization))
    print("移動平均の最大相関係数: "+str(biggest_corr_moving))
    

    

if __name__ == '__main__':
    user_read()
