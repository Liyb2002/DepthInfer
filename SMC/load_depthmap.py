import cv2
import numpy as np
import matplotlib.pyplot as plt
import json

import config

detph_map_path = './depthMap/predict.png'
file_name = './three/sample_points.json'
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
          dist = (sum_depthMap[i][j]-540) * 0.05
          pos_x = j * (5.0 / 256.0)
          pos_y = 5.0 - (i * (5.0 / 256.0))
          sample_point = np.array([pos_x, pos_y, dist[0]])
          # sample_point = cam.get_position(np.array([i,j]), dist)
          sample_points.append(sample_point)


def output_sample_pts (sample_points, file_name):
  result = []  
  for pt in sample_points:
      data = {'pt':
          {
          'x': float(pt[0]),
          'y': float(pt[1]),
          'z': float(pt[2]),
          }
          }
      result.append(data)

  with open(file_name, 'w') as f:
      json.dump(result, f, indent=2)


output_sample_pts(sample_points, file_name)
