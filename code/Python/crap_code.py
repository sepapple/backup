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
    USERPATH="/Users/sepa/SensorData/XYZUserData44.csv"
    CARPATH="/Users/sepa/SensorData/XYZCarData46.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData45.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData47.csv"
    # USERPATH="/Users/sepa/SensorData/XYZUserData46.csv"
    # CARPATH="/Users/sepa/SensorData/XYZCarData48.csv"
    userData = []
    carData = []
    user_synthetic = []
    car_synthetic = []
    dataset_normalization1 = []
    dataset_normalization2 = []
    dataset_normalization3 = []
    dataset_normalization4 = []
    dataset_normalization5 = []
    dataset_normalization6 = []
    dataset_normalization7 = []
    dataset_normalization8 = []
    dataset_normalization9 = []
    dataset_normalization10= []
    dataset_moving1 = []
    dataset_moving2 = []
    dataset_moving3 = []
    dataset_moving4 = []
    dataset_moving5 = []
    dataset_moving6 = []
    dataset_moving7 = []
    dataset_moving8 = []
    dataset_moving9 = []
    dataset_moving10= []
    temp = []
    biggest_corr_normalization = 0
    biggest_corr_moving = 0
    start = 0
    window = 10
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
    

    #1回目
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
        dataset_normalization1.append(temp)
        temp=[]
        i+=1
        print(i)

    df_normalization = pd.DataFrame(dataset_normalization1,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving1.append(temp)
        temp=[]
        i+=1
    df_moving = pd.DataFrame(dataset_moving1,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #2回目
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
        dataset_normalization2.append(temp)
        temp=[]
        i+=1
        print(i)

    print(dataset_normalization2)

    df_normalization2 = pd.DataFrame(dataset_normalization2,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization2.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization2.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization2.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving2.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving2,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #3回目
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
        dataset_normalization3.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization3,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving3.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving3,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #4回目
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
        dataset_normalization4.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization4,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving4.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving4,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #5回目
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
        dataset_normalization5.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization5,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving5.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving5,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #6回目
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
        dataset_normalization6.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization6,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving6.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving6,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #7回目
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
        dataset_normalization7.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization7,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving7.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving7,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #8回目
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
        dataset_normalization8.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization8,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving8.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving8,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)
    
    #9回目
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
        dataset_normalization9.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization9,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving9.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving9,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    user_synthetic.pop(0)

    #10回目
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
        dataset_normalization10.append(temp)
        temp=[]
        i+=1


    df_normalization = pd.DataFrame(dataset_normalization10,columns=['User','Car'],)
    print("正規化後の相関係数")
    print(df_normalization.corr())
    if(abs(biggest_corr_normalization) < abs(df_normalization.corr().iat[0,1])):
        biggest_corr_normalization = df_normalization.corr().iat[0,1]
    
    v = np.ones(window)/window
    user_ave = np.convolve(user_normalization,v,mode='same')
    car_ave = np.convolve(car_normalization,v,mode='same')
    i=0
    while(i<len(user_ave) and i<len(car_ave)):
        temp.append(float(user_ave[i]))
        temp.append(float(car_ave[i]))
        dataset_moving10.append(temp)
        temp=[]
        i+=1

    df_moving = pd.DataFrame(dataset_moving10,columns=['User','Car'],)
    print("移動平均の相関係数")
    print(df_moving.corr().iat[0,1])
    if(abs(biggest_corr_moving) < abs(df_moving.corr().iat[0,1])):
        biggest_corr_moving = df_moving.corr().iat[0,1]

    
    print("正規化の最大相関係数: " + str(biggest_corr_normalization))
    print("移動平均の最大相関係数: "+str(biggest_corr_moving))


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
