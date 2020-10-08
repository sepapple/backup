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
    # USERPATH="/Users/sepa/SensorData/XYZUserData54.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData61.csv"
    USERPATH="/Users/sepa/SensorData/XYZUserData55.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData62.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData56.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData63.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData57.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData64.csv"
    userData = []
    carData = []
    user_synthetic = []
    car_synthetic = []
    dataset_normalization = []
    dataset_moving = []
    temp = []
    start = 0
    window = 100
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
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    user_x = [i for i in range(len(user_synthetic))]
    car_x = [i for i in range(len(car_synthetic))]
    ax1.plot(user_x,user_synthetic,color='b',label='UserData') 
    ax1.set_xlim([start,start+len(user_synthetic)]) 
    ax1.set_ylim([np.min(user_synthetic), np.max(user_synthetic)]) 
    ax1.set_xlabel("count ",size=10)
    ax1.set_ylabel("synthetic accel",size=10)
    ax1.legend()
    
    ax2.plot(car_x,car_synthetic,color='r',label='CarData') 
    ax2.set_xlim([start,start+len(car_synthetic)]) 
    ax2.set_ylim([np.min(car_synthetic), np.max(car_synthetic)]) 
    ax2.legend()
    plt.show()
    """
    #正規化
    if (abs(np.max(user_synthetic)) >= abs(np.min(user_synthetic))):
            user_normalization = [y / np.max(user_synthetic) for y in user_synthetic]
    else:
            user_normalization = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

    if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
            car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
    else:
            car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]
    
    user_x = [i for i in range(len(user_normalization))]
    car_x = [i for i in range(len(car_normalization))]
    ax1.plot(user_x,user_normalization,color='b',label='UserData') 
    ax1.set_xlim([start,start+len(user_normalization)]) 
    ax1.set_ylim([np.min(user_normalization), np.max(user_normalization)]) 
    ax1.set_xlabel("count ",size=10)
    ax1.set_ylabel("normalization accel",size=10)
    ax1.legend()
    
    ax2.plot(car_x,car_normalization,color='r',label='CarData') 
    ax2.set_xlim([start,start+len(car_normalization)]) 
    ax2.set_ylim([np.min(car_normalization), np.max(car_normalization)]) 
    ax2.legend()
    plt.show()
    """

if __name__ == '__main__':
    read()
