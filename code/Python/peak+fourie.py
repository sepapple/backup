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
    # USERPATH="/Users/sepa/SensorData/XYZUserData45.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData47.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData46.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData48.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData47.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData49.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData48.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData50.csv"

    USERPATH="/Users/sepa/SensorData/XYZUserData52.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData58.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData53.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData60.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData54.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData61.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData55.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData62.csv"
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
    start = 0
    N = 100
    fs = 10 #10Hz
    window = 10
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

    # maxid = signal.argrelmax(user_ave,order=10)
    # minid = signal.argrelmin(car_ave,order=10)

    user_max = signal.argrelmax(np.array(user_normalization),order = order)
    car_max = signal.argrelmax(np.array(car_normalization),order = order)
    # minid = signal.argrelmin(np.array(car_normalization),order=10)


    # print(user_max)
    # print(minid)
    user_x = np.array([i for i in range(len(user_max[0]))])
    # x = np.array([i for i in range(start, start+len(user_max))])
    # x = np.array([i for i in range(start, start+len(user_normalization))])
    # y = np.array([user_normalization[i] for i in user_max.tolist()])    
    # y = np.array(user_normalization)    
    user_y = []
    for i in range(len(user_max[0])):
        user_y.append(user_normalization[user_max[0][i]])
    
    car_y = []
    for i in range(len(car_max[0])):
        car_y.append(car_normalization[car_max[0][i]])

    used_len = 0
    if(len(user_y)>len(car_y)):
        used_len = len(car_y)
    else:
        used_len = len(user_y)

    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)

    for slide in range(int(used_len/N)):
        hanningWindow = np.hanning(N)  
        # hanningWindow = np.hanning(len(user_y))  
        X = scipy.fftpack.fft(hanningWindow * user_y[start:start+N]) 
        # print(start+N)
        # X = scipy.fftpack.fft(hanningWindow * user_y[start:start+len(user_y)]) 

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
                # for j in range(int(len(user_y)/len(freqList))):
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
        # ax1.plot(range(start, len(user_y)), user_y[start:len(user_y)]) 
        # ax1.set_xlim([start, len(user_y)]) 
        ax1.plot(range(start, start+N), user_y[start:start+N]) 
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
        # hanningWindow = np.hanning(len(car_y))  
        # X = scipy.fftpack.fft(hanningWindow * car_ave[start:start+N]) 
        X = scipy.fftpack.fft(hanningWindow * car_y[start:start+N]) 
        # X = scipy.fftpack.fft(hanningWindow * car_y[start:start+len(car_y)]) 





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
                # for j in range(int(len(car_y)/len(freqList))):
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
        # ax3.plot(range(start, len(car_y)), car_y[start:len(car_y)]) 
        # ax3.set_xlim([start, len(car_normalaization]) 
        ax3.plot(range(start,start+N), car_y[start:start+N]) 
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
        plt.pause(5)
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
