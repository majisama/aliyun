
from keras.layers import Input,LSTM,GRU,Dense,Concatenate
from numpy import concatenate
from keras.models import Model,load_model
from keras.layers.core import Flatten
import keras
import numpy as np
import sys,os
class prd:
    def __init__(self):
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0])) 
        global model  
        keras.backend.clear_session() 
        model = load_model(dirname+"/model.h5")
        
    def prdt(self,data):
        samehours=np.log10(data[:144].reshape(6,24))
        prdts=np.array([])
        for i in range(0,3):
            #没办法了,重复使用会报错
            pd=model.predict([[samehours]])
            samehours=np.delete(samehours,0,axis=0) 
            samehours=np.append(samehours,pd[0][0])
            samehours=samehours.reshape(6,24)
            prdts=np.append(prdts,[pd])  
        return np.power(10,prdts)
            
            
