

# imports - numpy just to read data

import numpy as np 

from keras.layers import Dense

from keras.models import Sequential

# read the data so we can find the number of nodes in the input layer (n_cols)
predictors = np.loadtxt('predictors_data.csv', delimiters=',')

n_cols = predictors.shape[1]

# Sequential model - each layer connected only to the previous layer
model = Sequential()

# build up model layer at a time - 'Dense' layers are fully connected
model.add(Dense(100, activation-'relu', input_shape = (n_cols,)))

model.add(Dense(100, activation='relu'))

model.add(Dense(1))
