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
EPOCHS = 1
BATCH_SIZE = 5

scene_list = ['./DS/ZA/', './DS/tree/', './DS/temple/', './DS/factory/']
df = dataGen.load_data(scene_list)

optimizer = tf.keras.optimizers.Adam(
    learning_rate=LR,
    amsgrad=False,
)
model = model.DepthEstimationModel()

model.compile(optimizer)

train_loader = dataGen.DataGenerator(
    data=df[:2].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
validation_loader = dataGen.DataGenerator(
    data=df[2:3].reset_index(drop="true"), batch_size=BATCH_SIZE, dim=(HEIGHT, WIDTH)
)
model.fit(
    train_loader,
    epochs=EPOCHS,
    validation_data=validation_loader,
)

model.load_weights('path_to_my_weights')

print(model.summary())
# image_path = "./testings/2.jpg"
# image = visualize.load_single_img_toPredict(image_path)
# predict = model.predict(image)
# visualize.visualize_result(predict)