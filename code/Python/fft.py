import numpy as np
import pandas as pd
import csv
from scipy import signal
from pylab import *
import matplotlib.pyplot as plt
import sys
#import matplotlib.pyplot as plt
#import seaborn as sons

def read():
    # data = pd.read_csv("/Users/sepa/Desktop/Data.csv",header=0)
    # print(data.corr())
    # USERPATH="/Users/sepa/SensorData/UserAllData44.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData46.csv"
    # USERPATH="/Users/sepa/SensorData/UserAllData43.csv"
    CARPATH="/Users/sepa/SensorData/CarAllData44.csv"
    USERPATH="/Users/sepa/SensorData/UserAllData46.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData48.csv"
    userData = []
    carData = []
    dataset = []
    temp = []
    start = 0
    
    #データの読み込み
    userDF = pd.read_csv(USERPATH,header=0)
    carDF = pd.read_csv(CARPATH,header=0)
     
    #正規化
    userData = userDF.iloc[:, 3:14].values.flatten()
    if (abs(np.max(userData)) >= abs(np.min(userData))):
            userData = [y / np.max(userData) for y in userData]
    else:
            userData = [y / abs(np.min(userData)) for y in userData]

    carData = carDF.iloc[:, 3:14].values.flatten()
    if (abs(np.max(carData)) >= abs(np.min(carData))):
            carData = [y / np.max(carData) for y in carData]
    else:
            carData = [y / abs(np.min(carData)) for y in carData]

    #描画
    if(len(userData)>=len(carData)):
        plt.plot(range(start, start+len(carData)), userData[start:start+len(carData)],color='r',label='UserData')
        plt.plot(range(start, start+len(carData)), carData[start:start+len(carData)],color='b',label='CarData')
        axis([start, start+len(carData), -1.0, 1.0]) 
        xlabel("data number") 
        ylabel("z_accel") 
        plt.show() 
    else:
        plt.plot(range(start, start+len(userData)), userData[start:start+len(userData)],color='r',label='UserData')
        plt.plot(range(start, start+len(userData)), carData[start:start+len(userData)],color='b',label='CarData')
        axis([start, start+len(userData), -1.0, 1.0]) 
        xlabel("data number") 
        ylabel("z_accel") 
        plt.show() 

    """
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
