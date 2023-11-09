import os
import sys
import tensorflow as tf
from tensorflow.keras import layers
import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt

import dataGen

path = "./DS/Image/0.png"
img = cv2.imread(path)
print(img.shape)

# filename = 'savedImage.jpg'
# cv2.imwrite(filename, img) 

path = "./DS/Image"
img_filelist = []
for root, dirs, files in os.walk(path):
    for file in files:
        if file == ".DS_Store":
            continue
        img_filelist.append(os.path.join(root, file))


img_filelist.sort()
path = "./DS/DepthMap"
depth_filelist = []
for root, dirs, files in os.walk(path):
    for file in files:
        depth_filelist.append(os.path.join(root, file))

depth_filelist.sort()



data = {
    "image": [x for x in img_filelist],
    "depth": [x for x in depth_filelist],
}
df = pd.DataFrame(data)

df = df.sample(frac=1, random_state=42)


HEIGHT = 256
WIDTH = 256
LR = 0.0002
EPOCHS = 30
BATCH_SIZE = 32


visualize_samples = next(
    iter(dataGen.DataGenerator(data=df, batch_size=6, dim=(HEIGHT, WIDTH)))
)
