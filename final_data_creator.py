import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle

train_data = np.load('training_data.npy')
train_data2 = np.load('training_data2.npy')

df = pd.DataFrame(train_data)
df2 = pd.DataFrame(train_data2)
print(df.head())
print(Counter(df[1].apply(str)))
print(Counter(df2[1].apply(str)))


left = []
right = []
up = []
shoot = []

shuffle(train_data)
shuffle(train_data2)

for data in train_data:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0,0,0]:
        left.append([img,choice])
    elif choice == [0,1,0,0,0]:
        up.append([img,choice])
    elif choice == [0,0,1,0,0]:
        right.append([img,choice])
    elif choice == [0,0,0,1,0]:
        shoot.append([img,choice])

for data in train_data2:
    img = data[0]
    choice = data[1]

    if choice == [1,0,0,0,0]:
        left.append([img,choice])
    elif choice == [0,1,0,0,0]:
        up.append([img,choice])
    elif choice == [0,0,1,0,0]:
        right.append([img,choice])
    elif choice == [0,0,0,1,0]:
        shoot.append([img,choice])

# Since right is the most dominant choice

lenn = min(len(up),len(left))
print(lenn)
up = up[:lenn]
right = right[:lenn]
left = left[:lenn]

finale = up+left+right+shoot
shuffle(finale)
np.save('train_data_finale.npy',finale)


