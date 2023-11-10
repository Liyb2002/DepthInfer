import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
import cv2
import os
import pandas as pd


def load_data():
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
    return df



class DataGenerator(tf.keras.utils.Sequence):
    def __init__(self, data, batch_size=6, dim=(256, 256), n_channels=3, shuffle=True):
        """
        Initialization
        """
        self.data = data
        self.indices = self.data.index.tolist()
        self.dim = dim
        self.n_channels = n_channels
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.min_depth = 0.1
        self.on_epoch_end()

    def __len__(self):
        return int(np.ceil(len(self.data) / self.batch_size))

    def __getitem__(self, index):
        if (index + 1) * self.batch_size > len(self.indices):
            self.batch_size = len(self.indices) - index * self.batch_size
        # Generate one batch of data
        # Generate indices of the batch
        index = self.indices[index * self.batch_size : (index + 1) * self.batch_size]
        # Find list of IDs
        batch = [self.indices[k] for k in index]
        x, y = self.data_generation(batch)

        return x, y

    def on_epoch_end(self):

        """
        Updates indexes after each epoch
        """
        self.index = np.arange(len(self.indices))
        if self.shuffle == True:
            np.random.shuffle(self.index)

    def load(self, image_path, depth_map):
        """Load input and target image."""

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = cv2.resize(image, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
        image = image.astype('float32') / 255.0


        depth_map = cv2.imread(depth_map)
        depth_map = cv2.cvtColor(depth_map, cv2.COLOR_BGR2RGB)
        depth_map = cv2.resize(depth_map, dsize=(256, 256), interpolation=cv2.INTER_CUBIC)
        depth_map = depth_map.astype('float32') / 255.0
        depth_map = depth_map.mean(axis=2, keepdims=True)

        return image, depth_map

    def data_generation(self, batch):

        x = np.empty((self.batch_size, *self.dim, self.n_channels))
        y = np.empty((self.batch_size, *self.dim, 1))

        for i, batch_id in enumerate(batch):
            x[i,], y[i,] = self.load(
                self.data["image"][batch_id],
                self.data["depth"][batch_id],
            )

        print("x.shape", x.shape)
        return x, y
