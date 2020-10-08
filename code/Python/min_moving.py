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

    # USERPATH="/Users/sepa/SensorData/XYZUserData55.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData62.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData56.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData63.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData57.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData64.csv"
    USERPATH="/Users/sepa/SensorData/XYZUserData58.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData65.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData59.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData66.csv"
    userData = []
    carData = []
    user_synthetic = []
    car_synthetic = []
    dataset_normalization = []
    dataset_moving = []
    temp = []
    start = 0
    window = 10
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
            user_normalization = [y / np.max(user_synthetic) for y in user_synthetic]
    else:
            user_normalization = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

    if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
            car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
    else:
            car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]

    while(i<len(user_normalization) and i<len(car_normalization)):
        temp.append(float(user_normalization[i]))
        temp.append(float(car_normalization[i]))
        dataset_normalization.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
    # print("正規化後の相関係数")
    # print(df_normalization.corr())
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')

    # maxid = signal.argrelmax(user_ave,order=10)
    # minid = signal.argrelmin(car_ave,order=10)

    user_min = signal.argrelmin(np.array(user_normalization),order = order)
    car_min = signal.argrelmin(np.array(car_normalization),order = order)
    # minid = signal.argrelmin(np.array(car_normalization),order=10)


    # print(user_min)
    # print(minid)
    user_x = np.array([i for i in range(len(user_min[0]))])
    # x = np.array([i for i in range(start, start+len(user_min))])
    # x = np.array([i for i in range(start, start+len(user_normalization))])
    # y = np.array([user_normalization[i] for i in user_min.tolist()])    
    # y = np.array(user_normalization)    
    user_y = []
    for i in range(len(user_min[0])):
        user_y.append(user_normalization[user_min[0][i]])
    
    
    #移動平均を取得
    v = np.ones(window)/window
    user_ave = np.convolve(user_y,v,mode='same')

    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    # user_y = np.array(user_y)
    user_x = [i for i in range(len(user_y))]
    # ax1.plot(range(start, start+len(user_ave)), user_ave[start:start+len(user_ave)],label='UserData') 
    # ax1.plot(x, user_normalization[start:start+len(user_normalization)],label='UserData') 
    ax1.plot(user_x,user_ave,color='b',label='UserData') 
    # ax1.plot(x[minid],y[minid],'ro',label='ピーク値')
    # ax1.plot(x[minid],y[minid],'bo',label='ピーク値(最小)')
    # ax1.set_xlim([start,start+len(user_normalization)]) 
    ax1.set_xlim([start,start+len(user_y)]) 
    ax1.set_ylim([-1.0, 1.0]) 
    # ax1.plot(x[minid],
    ax1.set_xlabel("count ",size=10)
    ax1.set_ylabel("synthetic accel",size=10)
    ax1.legend()

    car_x = np.array([i for i in range(len(car_min[0]))])
    car_y = []
    for i in range(len(car_min[0])):
        car_y.append(car_normalization[car_min[0][i]])

    #移動平均
    car_x = [i for i in range(len(car_y))]
    car_ave = np.convolve(car_y,v,mode='same')

    ax2.plot(car_x,car_ave,color='r',label='CarData') 
    ax2.set_xlim([start,start+len(car_y)]) 
    ax2.set_ylim([-1.0, 1.0]) 
    ax2.legend()

    for slide in range(list_window):
        i=0
        dataset_normalization = []
        while(i<len(user_ave) and i<len(car_ave)):
            temp.append(user_ave[i])
            temp.append(car_ave[i])
            dataset_normalization.append(temp)
            temp=[]
            i+=1
    
        df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
        print("User側移動平均後の相関係数スライド数: "+ str(slide+1))
        print(df_normalization.corr())
        user_ave = np.delete(user_ave,0)
        # user_ave.pop(0)     
        if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
            biggest_corr_normalization = df_normalization.corr().iat[0,1]


    user_ave = np.convolve(user_y,v,mode='same')

    for slide in range(list_window):
        i=0
        dataset_normalization = []
        while(i<len(user_ave) and i<len(car_ave)):
            temp.append(user_ave[i])
            temp.append(car_ave[i])
            dataset_normalization.append(temp)
            temp=[]
            i+=1
    
        df_normalization = pd.DataFrame(dataset_normalization,columns=['User','Car'],)
        print("Car側移動平均後の相関係数スライド数: "+ str(slide+1))
        print(df_normalization.corr())
        car_ave = np.delete(car_ave,0)
        # car_y.pop(0)     

        if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
            biggest_corr_normalization = df_normalization.corr().iat[0,1]

    print("移動平均の最大相関係数: " + str(biggest_corr_normalization))
    plt.show()

if __name__ == '__main__':
    read()
