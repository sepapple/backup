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
    # USERPATH="/Users/sepa/SensorData/XYZUserData42.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData40.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData44.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData46.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData46.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData48.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData47.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData49.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData48.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData50.csv"

    #10Hz
    USERPATH="/Users/sepa/SensorData/XYZUserData52.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData58.csv"
    userData = []
    carData = []
    dataset = []
    temp = []
    user_normalization =[]
    car_normalization =[]
    start = 0
    N = 49
    # fs = 5 #5Hz
    fs = 10#5Hz
    window = 10
    i=0

    #データの読み込み
    userDF = pd.read_csv(USERPATH,header=0)
    carDF = pd.read_csv(CARPATH,header=0)

    x_userData = userDF.iloc[:, 3:13].values.flatten()
    y_userData = userDF.iloc[:, 13:23].values.flatten()
    z_userData = userDF.iloc[:, 23:33].values.flatten()
    
    x_carData = carDF.iloc[:, 3:13].values.flatten()
    y_carData = carDF.iloc[:, 13:23].values.flatten()
    z_carData = carDF.iloc[:, 23:33].values.flatten()

    user_synthetic = [np.sqrt(x_userData[i]**(2)+y_userData[i]**(2)+z_userData[i]**(2)) for i in range(0,len(x_userData))]
    car_synthetic = [np.sqrt(x_carData[i]**(2)+y_carData[i]**(2)+z_carData[i]**(2)) for i in range(0,len(x_carData))]

    #正規化
    """
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

    """

    #合成加速度

    if (abs(np.max(user_synthetic)) >= abs(np.min(user_synthetic))):
            user_normalization = [y / np.max(user_synthetic) for y in user_synthetic]
    else:
            user_normalization = [y / abs(np.min(user_synthetic)) for y in user_synthetic]

    if (abs(np.max(car_synthetic)) >= abs(np.min(car_synthetic))):
            car_normalization = [y / np.max(car_synthetic) for y in car_synthetic]
    else:
            car_normalization = [y / abs(np.min(car_synthetic)) for y in car_synthetic]

    
    #移動平均を取得
    """
    v = np.ones(window)/window
    user_ave = np.convolve(userData,v,mode='same')
    car_ave = np.convolve(carData,v,mode='same')
    """

    # userlen = len(userData)
    # carlen = len(carData)


    
    #相関分析
    # df = pd.DataFrame(dataset,columns=['User','Car'],)
    # print(df.corr())

    #描画
    #figure()でグラフを表示する領域を作成
    fig = plt.figure()

    #add_subplot()でグラフを描画する領域を追加
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    
    used_len = 0
    if(len(user_normalization)>len(car_normalization)):
        used_len = len(car_normalization)
    else:
        used_len = len(user_normalization)
    

    #ユーザ側
    # ハニングウィンドウ
    for slide in range(int(used_len/N)):
        hanningWindow = np.hanning(N)  
        # hanningWindow = np.hanning(len(user_normalization))  
        X = scipy.fftpack.fft(hanningWindow * user_normalization[start:start+N]) 
        # print(start+N)
        # X = scipy.fftpack.fft(hanningWindow * user_normalization[start:start+len(user_normalization)]) 

        # 周波数軸の値を計算 
        temp = []
        temp_value = 0
        # freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)
        freqList = ['{:.1f}'.format(i*0.1+0.1) for i in range(fs*5)]
        # 振幅スペクトル
        amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
        if(N>=len(freqList)):
            for i in range(len(freqList)):
                for j in range(int(N/len(freqList))):
                # for j in range(int(len(user_normalization)/len(freqList))):
                    temp_value += amplitudeSpectrum[i*int(N/(len(freqList)))+j]
                temp.append(temp_value/int(N/len(freqList)))
                temp_value = 0
            freqList.pop(0)
            freqList.pop(0)
            freqList.pop(len(freqList)-1)
            temp.pop(len(temp)-1)
            temp.pop(0)
        else:
            freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)
            roop_count = int(len(freqList)/2)
            for i in range(roop_count):
                freqList = np.delete(freqList,len(freqList)-1)
                amplitudeSpectrum.pop(len(amplitudeSpectrum)-1) 
            freqList = np.delete(freqList,0)
            temp = amplitudeSpectrum
        temp.pop(0)
        user = temp

        #元の波形
        # print(amplitudeSpectrum)
        # print(freqList)
        # print(len(amplitudeSpectrum))
        # plot(range(start, start+N), user_ave[start:start+N]) 
        # ax1.plot(range(start, len(user_normalization)), user_normalization[start:len(user_normalization)]) 
        # ax1.set_xlim([start, len(user_normalization)]) 
        ax1.plot(range(start, start+N), user_normalization[start:start+N]) 
        ax1.set_xlim([start,start+N]) 
        ax1.set_ylim([-1.0, 1.0]) 
        ax1.set_xlabel("count ",size=10)
        ax1.set_ylabel("synthetic accel",size=10)
        # axis([start, start+N, -1.0, 1.0]) 
        # xlabel("data number") 
        # ylabel("amplitude") 
        # plt.show() 

        # 振幅スペクトル 
        # ax1.plot(freqList, amplitudeSpectrum, marker= '.', linestyle='-',color='r',linewidth=0.3) 
        ax2.plot(freqList,temp, marker= '.', linestyle='-',color='r',linewidth=0.3,label='UserData') 
        # axis([0, fs/2, 0, np.max(amplitudeSpectrum)]) 
        if(N>=fs*5):
            ax2.set_xlim([0, fs*5+5]) 
        else:
            ax2.set_xlim([0, fs/2+0.5]) 

        ax2.set_ylim([0, 2]) 
        ax2.set_xlabel("frequency [Hz]",size=10)
        ax2.set_ylabel("amplitude spectrum",size=10)
        # xlabel("frequency [Hz]") 
        # ylabel("amplitude spectrum") 
        # plt.show()

        #車側
        hanningWindow = np.hanning(N)  
        # hanningWindow = np.hanning(len(car_normalization))  
        # X = scipy.fftpack.fft(hanningWindow * car_ave[start:start+N]) 
        X = scipy.fftpack.fft(hanningWindow * car_normalization[start:start+N]) 
        # X = scipy.fftpack.fft(hanningWindow * car_normalization[start:start+len(car_normalization)]) 





        # 周波数軸の値を計算 
        freqList = ['{:.1f}'.format(i*0.1+0.1) for i in range(fs*5)]
        # freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)
        # print(freqList)
        # 振幅スペクトル
        temp = []
        temp_value = 0
        amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
        if(N>=len(freqList)):
            for i in range(len(freqList)):
                for j in range(int(N/len(freqList))):
                # for j in range(int(len(car_normalization)/len(freqList))):
                    temp_value += amplitudeSpectrum[i*int(N/len(freqList))+j]
                temp.append(temp_value/int(N/len(freqList)))
                temp_value = 0
            freqList.pop(0)
            freqList.pop(0)
            freqList.pop(len(freqList)-1)
            temp.pop(0)
            temp.pop(len(temp)-1)
        else:
            freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)
            roop_count = int(len(freqList)/2)
            for i in range(roop_count):
                freqList = np.delete(freqList,len(freqList)-1)
                amplitudeSpectrum.pop(len(amplitudeSpectrum)-1) 
            freqList = np.delete(freqList,0)
            temp = amplitudeSpectrum
        #元の波形
        temp.pop(0)
        car = temp
        # plot(range(start, start+N), car_ave[start:start+N]) 
        # axis([start, start+N, -1.0, 1.0]) 
        # xlabel("data number") 
        # ylabel("amplitude") 
        # plt.show() 
        # ax3.plot(range(start, len(car_normalization)), car_normalization[start:len(car_normalization)]) 
        # ax3.set_xlim([start, len(car_normalaization]) 
        ax3.plot(range(start,start+N), car_normalization[start:start+N]) 
        ax3.set_xlim([start, start+N]) 
        ax3.set_ylim([-1.0, 1.0]) 
        ax3.set_xlabel("count ",size=10)
        ax3.set_ylabel("synthetic accel",size=10)

        # 振幅スペクトル 
        # ax2.plot(freqList, amplitudeSpectrum, marker= '.', linestyle='-',color='b',linewidth=0.3) 
        ax4.plot(freqList, temp, marker= '.', linestyle='-',color='b',linewidth=0.3,label='CarData') 
        # axis([0, fs/2, 0, np.max(amplitudeSpectrum)]) 
        # ax4.set_xlim([0, 30])
        if(N>=fs*5):
            ax4.set_xlim([0, fs*5+5])
        else:
            ax4.set_xlim([0, fs/2+0.5]) 
        ax4.set_ylim([0, 2]) 
        ax4.set_xlabel("frequency [Hz]",size=10)
        ax4.set_ylabel("amplitude spectrum",size=10)
        # xlabel("frequency [Hz]") 
        # ylabel("amplitude spectrum") 
        plt.setp(ax2.get_xticklabels(),rotation=0)
        plt.setp(ax4.get_xticklabels(),rotation=0)
        ax2.legend()
        ax4.legend()
        plt.pause(1)
        # plt.show()
        # plt.cla()
        ax2.cla()
        ax4.cla()
        dataset = []
        val = []
        # print(user)
        # print(car)


        for i in range(len(user)):
            val.append(user[i])
            val.append(car[i])
            dataset.append(val)
            val = []
            
        # print(dataset)
        df = pd.DataFrame(dataset,columns=['User','Car'])
        print(df.corr())
        # userNum = len(userData)
        # carNum = len(carData)
        start += N

    

if __name__ == '__main__':
    read()
    iser_normalization =[]
    car_normalization =[]
