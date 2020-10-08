import numpy as np
import pandas as pd
#import seaborn as sons

def read():
    data = pd.read_csv("/Users/sepa/Desktop/Data.csv",header=0)
    # print(data)
    print(data.corr())

if __name__ == '__main__':
    read()
