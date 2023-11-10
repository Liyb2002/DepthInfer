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
BATCH_SIZE = 5

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

model.load_weights('path_to_my_weights')

image_path = "./DS/Image/10.png"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
image = image.astype('float32') / 255.0
reshaped_array = image[np.newaxis, ...]

#shape (1, 256, 256, 1)
predict = model.predict(reshaped_array)


visualize.visualize_result(predict)