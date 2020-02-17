import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error

def load_model_lasso():
    result = None
    try:
        print("================Modeling================")
        df = pd.read_csv('model_data.csv', encoding = 'cp949')
        
        # Missing Data 처리
        df2 = df.dropna()
        #X, Y 설정
        X = df2[['AGE','WEIGHT','RUNTIME','RUNPULSE','RSTPULSE','MAXPULSE']]
        Y = df2[['OXY']]
        # Train / Test Split
        X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size =.3)
        #학습
        model = Lasso()
        result = model.fit(X_train, Y_train)
    except Exception as e:
        print(e)
    finally :
        pass

    return result




