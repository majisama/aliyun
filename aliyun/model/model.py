
from keras.layers import Input,LSTM,GRU,Dense,Concatenate
from numpy import concatenate
from keras.models import Model,load_model
from keras.layers.core import Flatten
from keras.layers import Reshape
hours=Input(shape=(6,24,),name="hours")
x=LSTM(36,activation='tanh',return_sequences=True)(hours)
x=LSTM(24,activation='relu')(x)
x=Reshape((1,24))(x)
x=Dense(48)(x)
output=Dense(24)(x)
model=Model(inputs=[hours], outputs=output)
model.summary()
