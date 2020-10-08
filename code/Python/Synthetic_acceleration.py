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
    CARPATH="/Users/sepa/SensorData/XYZCarData50.csv"
    USERPATH="/Users/sepa/SensorData/XYZUserData52.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData58.csv"
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
    print("正規化後の相関係数")
    print(df_normalization.corr())
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2)
    #相関分析
    if(len(user_synthetic)>=len(car_synthetic)):
        ax1.plot(range(start, start+len(car_synthetic)), user_synthetic[start:start+len(car_synthetic)],color='r',label='UserData')
        ax2.plot(range(start, start+len(car_synthetic)), car_synthetic[start:start+len(car_synthetic)],color='b',label='CarData')
        # ax1.plot(range(start, start+len(car_synthetic)), car_synthetic[start:start+len(car_synthetic)],color='b',label='CarData')
        # ax2.plot(range(start, start+len(car_normalization)), user_normalization[start:start+len(car_normalization)],color='r',label='UserData')
        # ax2.plot(range(start, start+len(car_normalization)), car_normalization[start:start+len(car_normalization)],color='b',label='CarData')
        # plt.plot(range(start, start+len(car_ave)), user_ave[start:start+len(car_ave)],color='r',label='UserData')
        # plt.plot(range(start, start+len(car_ave)), car_ave[start:start+len(car_ave)],color='b',label='CarData')
        # axis([start, start+len(car_ave), -1.0,1.0]) 
        # axis([start, start+len(car_synthetic), np.min(car_synthetic)-5.0,np.max(car_synthetic)+5.0]) 
        ax1.set_xlabel("data_number",size=10)
        ax1.set_ylabel("Synthetic_Accel",size=10)
        ax2.set_xlabel("data_number",size=10)
        ax2.set_ylabel("Synthetic_Accel",size=10)
        # xlabel("data number") 
        # ylabel("z_accel") 
        # plt.legend()
        ax1.legend()
        ax2.legend()
        plt.show() 
    else:
        ax1.plot(range(start, start+len(user_synthetic)), user_synthetic[start:start+len(user_synthetic)],color='r',label='UserData')
        ax2.plot(range(start, start+len(user_synthetic)), car_synthetic[start:start+len(user_synthetic)],color='b',label='CarData')
        # ax1.plot(range(start, start+len(user_synthetic)), car_synthetic[start:start+len(user_synthetic)],color='b',label='CarData')
        # ax2.plot(range(start, start+len(user_ave)), user_ave[start:start+len(user_ave)],color='r',label='UserData')
        # ax2.plot(range(start, start+len(user_ave)), car_ave[start:start+len(user_ave)],color='b',label='CarData')
        # axis([start, start+len(user_ave), -1.0,1.0]) 
        # axis([start, start+len(user_synthetic), np.min(user_synthetic)-5.0,np.max(user_synthetic)+5.0]) 
        ax1.set_xlabel("data_number",size=10)
        ax1.set_ylabel("Synthetic_Accel",size=10)
        ax2.set_xlabel("data_number",size=10)
        ax2.set_ylabel("Synthetic_Accel",size=10)
        # xlabel("data number") 
        # ylabel("z_accel") 
        ax1.legend()
        ax2.legend()
        # plt.legend()
        plt.show() 

    # print(z_userData[9])
    # print(len(z_userData))
    #正規化
    """
    if (abs(np.max(x_userData)) >= abs(np.min(x_userData))):
            x_userData = [y / np.max(x_userData) for y in x_userData]
    else:
            x_userData = [y / abs(np.min(x_userData)) for y in x_userData]
    """

    """
    carData = carDF.iloc[:, 3:14].values.flatten()
    if (abs(np.max(carData)) >= abs(np.min(carData))):
            carData = [y / np.max(carData) for y in carData]
    else:
            carData = [y / abs(np.min(carData)) for y in carData]

    
    #移動平均を取得
    v = np.ones(window)/window
    user_ave = np.convolve(userData,v,mode='same')
    car_ave = np.convolve(carData,v,mode='same')

    userlen = len(user_ave)
    carlen = len(car_ave)


    #データセット作り
    while(i<userlen and i<carlen):
        for x in range(3,10):
            temp.append(float(user_ave[i]))
            temp.append(float(car_ave[i]))
            dataset.append(temp)
            temp=[]
        i+=1

    
    #相関分析
    df = pd.DataFrame(dataset,columns=['User','Car'],)
    print(df.corr())

    #描画
    if(len(userData)>=len(carData)):
        plt.plot(range(start, start+len(carData)), userData[start:start+len(carData)],color='r',label='UserData')
        plt.plot(range(start, start+len(carData)), carData[start:start+len(carData)],color='b',label='CarData')
        plt.plot(range(start, start+len(carData)), user_ave[start:start+len(carData)],color='g',label='user_ave')
        plt.plot(range(start, start+len(carData)), car_ave[start:start+len(carData)],color='k',label='car_ave')
        axis([start, start+len(carData), -1.0, 1.0])
        xlabel("data number") 
        ylabel("z_accel") 
        plt.legend()
        plt.show() 
    else:
        # plt.plot(range(start, start+len(userData)), userData[start:start+len(userData)],color='r',label='UserData')
        # plt.plot(range(start, start+len(userData)), carData[start:start+len(userData)],color='b',label='CarData')
        plt.plot(range(start, start+len(userData)), user_ave[start:start+len(userData)],color='g',label='user_ave')
        plt.plot(range(start, start+len(userData)), car_ave[start:start+len(userData)],color='k',label='car_ave')
        axis([start, start+len(userData), -1.0, 1.0]) 
        xlabel("data number") 
        ylabel("z_accel") 
        plt.legend()
        plt.show() 

    while num > 0:
            # ハニングウィンドウ
            hanningWindow = np.hanning(N)  
            X = scipy.fftpack.fft(hanningWindow * x[start:start+N]) 

            # 周波数軸の値を計算 
            freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)

            # 振幅スペクトル
            amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]

            # 元の波形 
            plot(range(start, start+N), x[start:start+N]) 
            axis([start, start+N, -1.0, 1.0]) 
            xlabel("data number") 
            ylabel("amplitude") 
            plt.show() 

            # 振幅スペクトル 
            plot(freqList, amplitudeSpectrum, marker= 'o', linestyle='-') 
            axis([0, fs/2, 0, np.max(amplitudeSpectrum)]) 
            xlabel("frequency [Hz]") 
            ylabel("amplitude spectrum") 
            plt.show()

            start = start + 10
            num = num - 1

    """
    # userNum = len(userData)
    # carNum = len(carData)

    

if __name__ == '__main__':
    read()
