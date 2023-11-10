import os
import sys
import tensorflow as tf
from tensorflow.keras import layers
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

import dataGen
import visualize
import model

HEIGHT = 256
WIDTH = 256
LR = 0.0002
EPOCHS = 5
BATCH_SIZE = 32

df = dataGen.load_data()

optimizer = tf.keras.optimizers.Adam(
    learning_rate=LR,
    amsgrad=False,
)
model = model.DepthEstimationModel()

model.compile(optimizer)

train_loader = dataGen.DataGenerator(
    data=df[:100].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
validation_loader = dataGen.DataGenerator(
    data=df[110:120].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
model.fit(
    train_loader,
    epochs=EPOCHS,
    validation_data=validation_loader,
)


# path = "./DS/Image/10.png"
# pred = model.predict(input)
# cv2.imwrite("pred", image[index]*255.0) 

model.save_weights('path_to_my_weights', save_format='tf')
