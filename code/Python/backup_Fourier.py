import numpy as np
import pandas as pd
import csv
import scipy.fftpack
from scipy import signal
from pylab import *
import matplotlib.pyplot as plt
#import matplotlib.pyplot as plt
#import seaborn as sons

def read():
    # data = pd.read_csv("/Users/sepa/Desktop/Data.csv",header=0)
    # print(data.corr())
    # USERPATH="/Users/sepa/SensorData/UserAllData44.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData46.csv"
    # USERPATH="/Users/sepa/SensorData/UserAllData43.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData44.csv"
    USERPATH="/Users/sepa/SensorData/UserAllData46.csv"
    # CARPATH="/Users/sepa/SensorData/CarAllData48.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData47.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData49.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData48.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData50.csv"
    userData = []
    carData = []
    dataset = []
    temp = []
    start = 0
    N = 500
    fs = 5 #5Hz
    window = 10
    i=0

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

    
    #移動平均を取得
    v = np.ones(window)/window
    user_ave = np.convolve(userData,v,mode='same')
    car_ave = np.convolve(carData,v,mode='same')

    # userlen = len(userData)
    # carlen = len(carData)
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
    # df = pd.DataFrame(dataset,columns=['User','Car'],)
    # print(df.corr())

    #描画
    """
    if(len(userData)>=len(carData)):
        plt.plot(range(0, 0+len(carData)), userData[0:0+len(carData)],color='r',label='UserData')
        plt.plot(range(0, 0+len(carData)), carData[0:0+len(carData)],color='b',label='CarData')
        plt.plot(range(0, 0+len(carData)), user_ave[0:0+len(carData)],color='g',label='user_ave')
        plt.plot(range(0, 0+len(carData)), car_ave[0:0+len(carData)],color='k',label='car_ave')
        axis([0, 0+len(carData), -1.0, 1.0])
        xlabel("data number") 
        ylabel("z_accel") 
        plt.legend()
        plt.show() 
    else:
        plt.plot(range(0, 0+len(userData)), userData[0:0+len(userData)],color='r',label='UserData')
        plt.plot(range(0, 0+len(userData)), carData[0:0+len(userData)],color='b',label='CarData')
        plt.plot(range(0, 0+len(userData)), user_ave[0:0+len(userData)],color='g',label='user_ave')
        plt.plot(range(0, 0+len(userData)), car_ave[0:0+len(userData)],color='k',label='car_ave')
        axis([start, start+len(userData), -1.0, 1.0]) 
        xlabel("data number") 
        ylabel("z_accel") 
        plt.legend()
        plt.show() 
    """
    #figure()でグラフを表示する領域を作成
    fig = plt.figure()

    #add_subplot()でグラフを描画する領域を追加
    ax1 = fig.add_subplot(1,2,1)
    ax2 = fig.add_subplot(1,2,2)
    
    #ユーザ側
    # ハニングウィンドウ
    hanningWindow = np.hanning(N)  
    # X = scipy.fftpack.fft(hanningWindow * user_ave[start:start+N]) 
    X = scipy.fftpack.fft(hanningWindow * user_ave[start:start+N]) 

    # 周波数軸の値を計算 
    freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)

    # 振幅スペクトル
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    # print(amplitudeSpectrum)
    print(freqList)
    print(len(amplitudeSpectrum))
    #元の波形

    # plot(range(start, start+N), user_ave[start:start+N]) 
    # axis([start, start+N, -1.0, 1.0]) 
    # xlabel("data number") 
    # ylabel("amplitude") 
    # plt.show() 

    # 振幅スペクトル 
    ax1.plot(freqList, amplitudeSpectrum, marker= '.', linestyle='-',color='r',linewidth=0.3) 
    # axis([0, fs/2, 0, np.max(amplitudeSpectrum)]) 
    ax1.set_xlim([0, 3]) 
    ax1.set_ylim([0, 3]) 
    ax1.set_xlabel("frequency [Hz]",size=10)
    ax1.set_ylabel("amplitude spectrum",size=10)
    # xlabel("frequency [Hz]") 
    # ylabel("amplitude spectrum") 
    # plt.show()

    #車側
    hanningWindow = np.hanning(N)  
    # X = scipy.fftpack.fft(hanningWindow * car_ave[start:start+N]) 
    X = scipy.fftpack.fft(hanningWindow * car_ave[start:start+N]) 

    # 周波数軸の値を計算 
    freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)

    # 振幅スペクトル
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]

    #元の波形

    # plot(range(start, start+N), car_ave[start:start+N]) 
    # axis([start, start+N, -1.0, 1.0]) 
    # xlabel("data number") 
    # ylabel("amplitude") 
    # plt.show() 

    # 振幅スペクトル 
    ax2.plot(freqList, amplitudeSpectrum, marker= '.', linestyle='-',color='b',linewidth=0.3) 
    # axis([0, fs/2, 0, np.max(amplitudeSpectrum)]) 
    ax2.set_xlim([0, 3]) 
    ax2.set_ylim([0, 3]) 
    ax2.set_xlabel("frequency [Hz]",size=10)
    ax2.set_ylabel("amplitude spectrum",size=10)
    # xlabel("frequency [Hz]") 
    # ylabel("amplitude spectrum") 
    plt.show()

    # userNum = len(userData)
    # carNum = len(carData)

    

if __name__ == '__main__':
    read()
