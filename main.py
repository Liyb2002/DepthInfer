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
EPOCHS = 8
BATCH_SIZE = 32

scene_list = ['./DS/ZA_Extended/', './DS/ZA/', './DS/tree/', './DS/temple/', './DS/factory/']
df = dataGen.load_data(scene_list)

split = int(len(df)*0.8)

optimizer = tf.keras.optimizers.Adam(
    learning_rate=LR,
    amsgrad=False,
)
model = model.DepthEstimationModel()

model.compile(optimizer)

train_loader = dataGen.DataGenerator(
    data=df[:split].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
validation_loader = dataGen.DataGenerator(
    data=df[split:].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
model.fit(
    train_loader,
    epochs=EPOCHS,
    validation_data=validation_loader,
)

# image_path = "./DS/Image/10.png"
# image = visualize.load_single_img_toPredict(image_path)
# predict = model.predict(image)
# visualize.visualize_result(predict)


model.save_weights('full_moedel', save_format='tf')
