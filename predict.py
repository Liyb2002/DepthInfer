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
EPOCHS = 2
BATCH_SIZE = 32

optimizer = tf.keras.optimizers.Adam(
    learning_rate=LR,
    amsgrad=False,
)
model = model.DepthEstimationModel()

model.compile(optimizer)

df = dataGen.load_data()
train_loader = dataGen.DataGenerator(
    data=df[:10].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
validation_loader = dataGen.DataGenerator(
    data=df[10:12].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
model.fit(
    train_loader,
    epochs=EPOCHS,
    validation_data=validation_loader,
)

print(model.summary())

model.load_weights('path_to_my_weights.h5', by_name = True, skip_mismatch = True)