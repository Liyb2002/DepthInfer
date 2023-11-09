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
EPOCHS = 30
BATCH_SIZE = 32

df = dataGen.load_data()


# visualize_samples = next(
#     iter(dataGen.DataGenerator(data=df, batch_size=6, dim=(HEIGHT, WIDTH)))
# )
# visualize.visualize_ds(visualize_samples)


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
