import numpy as np
import pandas as pd
df = pd.read_csv('Churn_Modelling.csv')
df.head()
df.drop(columns = ['RowNumber','CustomerId','Surname'],inplace=True)
df.head()
df['Geography'].value_counts()
df = pd.get_dummies(df,columns=['Geography','Gender'],drop_first=True)
X = df.drop(columns=['Exited']) 
y = df['Exited'].values

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train_trf = scaler.fit_transform(X_train)
X_test_trf = scaler.transform(X_test)
import tensorflow
from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()

model.add(Dense(11,activation='sigmoid',input_dim=11))
model.add(Dense(11,activation='sigmoid'))
model.add(Dense(1,activation='sigmoid'))
model.summary()
  model.compile(optimizer='Adam',loss='binary_crossentropy',metrics=['accuracy'])
history = model.fit(X_train,y_train,batch_size=50,epochs=100,verbose=1,validation_split=0.2)
y_pred = model.predict(X_test)
y_pred
y_pred = y_pred.argmax(axis=-1)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred)
import matplotlib.pyplot as plt

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
