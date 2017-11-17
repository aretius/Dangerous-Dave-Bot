from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Input
from keras.layers import Conv2D
from keras.layers import Dropout
from keras.layers import MaxPooling2D
from keras.layers import GlobalMaxPooling2D
from keras.layers import GlobalAveragePooling2D
from keras.preprocessing import image
from keras.utils import layer_utils
from keras.utils.data_utils import get_file
from keras import backend as K
from keras.optimizers import SGD
import numpy as np
from keras.callbacks import ModelCheckpoint

WIDTH = 80
HEIGHT = 60

model = Sequential()
model.add(Conv2D(32, (3,3),activation = 'relu',input_shape=(80,60,1)))
model.add(Conv2D(32, (3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3,3),activation = 'relu'))
model.add(Conv2D(64, (3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, (3,3),activation = 'relu'))
model.add(Conv2D(128, (3,3),activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512,activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(5,activation = 'softmax'))

#sgd = SGD(lr = 1e-3, decay=1e-6, momentum = 0.9, nesterov = True)
model.compile(loss = 'categorical_crossentropy',optimizer = 'rmsprop',metrics = ['accuracy'])

train_data = np.load('train_data_finale.npy')
train = train_data[:-400]
test = train_data[-400:]

X = np.array([i[0] for i in train]).reshape(-1,WIDTH,HEIGHT,1)
Y = [i[1] for i in train]

test_x = np.array([i[0] for i in test]).reshape(-1,WIDTH,HEIGHT,1)
test_y = [i[1] for i in test]

print(len(X))
print(len(test_x))

checkpointer = ModelCheckpoint(filepath='first_model_weights_nvgg.hdf5', verbose=1, save_best_only=True)

model.fit(X, Y, batch_size=16, epochs=50,validation_data = (test_x,test_y),callbacks = [checkpointer])
