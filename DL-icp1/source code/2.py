import pandas
from pathlib import Path
from keras.models import Sequential
from keras.layers.core import Dense, Activation

# load dataset
from sklearn.model_selection import train_test_split
import pandas as pd
df = pd.read_csv(Path("Breas Cancer.csv"))
# print(dataset)
df["diagnosis"]= df["diagnosis"].replace("M",0)
df["diagnosis"]= df["diagnosis"].replace("B",1)
import numpy as np
X_train, X_test, Y_train, Y_test = train_test_split(df.iloc[:,2:32], df.iloc[:,1],
                                                    test_size=0.25, random_state=30)

# print(dataset.shape)

np.random.seed(155)
my_first_nn = Sequential() # create model
my_first_nn.add(Dense(40, input_dim=30, activation='relu')) # hidden layer
my_first_nn.add(Dense(25, input_dim=30,  activation='tanh'))
my_first_nn.add(Dense(8, input_dim=20, activation='relu'))
my_first_nn.add(Dense(1, input_dim=29,activation='sigmoid')) # output layer
my_first_nn.compile(loss='binary_crossentropy', optimizer='adam')
my_first_nn_fitted = my_first_nn.fit(X_train, Y_train, epochs=100, verbose=0,
                                     initial_epoch=0)
print(my_first_nn.summary())
print(my_first_nn.evaluate(X_test, Y_test, verbose=0))