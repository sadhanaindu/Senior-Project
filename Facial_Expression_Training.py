#!/usr/bin/env python
# coding: utf-8

# <h2 align=center> Facial Expression Recognition</h2>

#  

# ### Task 1: Import Libraries

# In[3]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import utils
import os
get_ipython().run_line_magic('matplotlib', 'inline')

from keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.layers import Dense, Input, Dropout,Flatten, Conv2D
from tensorflow.python.keras.layers import BatchNormalization, Activation, MaxPooling2D # Import error. 
from tensorflow.python.keras.models import Model, Sequential
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from tensorflow.python.keras.utils import plot_model
# from tensorflow.python.keras.layers import BatchNormalization

from IPython.display import SVG, Image
from livelossplot import PlotLossesKerasTF
import tensorflow as tf
print("Tensorflow version:", tf.__version__)


# ### Task 2: Plot Sample Images

# In[2]:


utils.datasets.fer.plot_example_images(plt).show()


# In[3]:


for expression in os.listdir("user_train/"):
    print(str(len(os.listdir("user_train/" + expression))) + " " + expression + " images")


# ### Task 3: Generate Training and Validation Batches

# In[4]:


img_size = 48
batch_size = 64

datagen_train = ImageDataGenerator(horizontal_flip=True)

train_generator = datagen_train.flow_from_directory("user_train/",
                                                    target_size=(img_size,img_size),
                                                    color_mode="grayscale",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=True)

datagen_validation = ImageDataGenerator(horizontal_flip=True)
validation_generator = datagen_validation.flow_from_directory("user_test/",
                                                    target_size=(img_size,img_size),
                                                    color_mode="grayscale",
                                                    batch_size=batch_size,
                                                    class_mode='categorical',
                                                    shuffle=False)


#  

# ### Task 4: Create CNN Model

# In[6]:


# Initialising the CNN
model = Sequential()

# 1 - Convolution
model.add(Conv2D(64,(3,3), padding='same', input_shape=(48, 48,1)))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 2nd Convolution layer
model.add(Conv2D(128,(5,5), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 3rd Convolution layer
model.add(Conv2D(512,(3,3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# 4th Convolution layer
model.add(Conv2D(512,(3,3), padding='same'))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Flattening
model.add(Flatten())

# Fully connected layer 1st layer
model.add(Dense(256))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.25))

# Fully connected layer 2nd layer
model.add(Dense(512))
model.add(BatchNormalization())
model.add(Activation('relu'))
model.add(Dropout(0.25))

model.add(Dense(7, activation='softmax'))

opt = Adam(lr=0.0005)
model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


#  

#  

# ### Task 6: Train and Evaluate Model

# In[7]:


get_ipython().run_cell_magic('time', '', '\nepochs = 15\nsteps_per_epoch = train_generator.n//train_generator.batch_size\nvalidation_steps = validation_generator.n//validation_generator.batch_size\n\nreduce_lr = ReduceLROnPlateau(monitor=\'val_loss\', factor=0.1,\n                              patience=2, min_lr=0.00001, mode=\'auto\')\ncheckpoint = ModelCheckpoint("model_weights.h5", monitor=\'val_accuracy\',\n                             save_weights_only=True, mode=\'max\', verbose=1)\ncallbacks = [PlotLossesKerasTF(), checkpoint, reduce_lr]\n\nhistory = model.fit(\n    x=train_generator,\n    steps_per_epoch=steps_per_epoch,\n    epochs=epochs,\n    validation_data = validation_generator,\n    validation_steps = validation_steps,\n    callbacks=callbacks\n)\n')


#  

# ### Task 7: Represent Model as JSON String

# In[8]:


model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)


# In[ ]:




