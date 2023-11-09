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


HEIGHT = 256
WIDTH = 256
LR = 0.0002
EPOCHS = 30
BATCH_SIZE = 32

df = dataGen.load_data()


visualize_samples = next(
    iter(dataGen.DataGenerator(data=df, batch_size=6, dim=(HEIGHT, WIDTH)))
)



visualize.visualize_ds(visualize_samples)