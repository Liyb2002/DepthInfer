import cv2
import numpy as np
import matplotlib.pyplot as plt

import config

detph_map_path = './depthMap/predict.png'
depth_map = cv2.imread(detph_map_path)

sum_depthMap = np.sum(depth_map, axis=2, keepdims=True)
sum_depthMap = sum_depthMap.astype(float)
smallest_element = np.min(sum_depthMap)
smallest_element = smallest_element - 20

cam = config.ortho_camera()
sample_points = []

for i in range (0, sum_depthMap.shape[0]):
    for j in range (0, sum_depthMap.shape[1]):
        if sum_depthMap[i][j] >720:
          continue
        else:
          dist = (sum_depthMap[i][j]- 540) * 0.05
          sample_point = cam.get_position(np.array([i,j]), dist)
          sample_points.append(sample_point)




