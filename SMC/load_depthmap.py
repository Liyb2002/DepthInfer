import cv2
import numpy as np
import matplotlib.pyplot as plt
import json
from scipy.ndimage import zoom

import rotate_samples
import config

def load_depth_map():
  detph_map_path = './depthMap/10.jpg'
  file_name = './three/sample_points.json'
  depth_map = cv2.imread(detph_map_path)

  sum_depthMap = np.sum(depth_map, axis=2, keepdims=True)
  sum_depthMap = sum_depthMap.astype(float)
  sum_depthMap = resize_depth_map(sum_depthMap)
  
  smallest_element = np.min(sum_depthMap)
  smallest_element = smallest_element - 20
  
  for i in range (0, sum_depthMap.shape[0]):
    for j in range (0, sum_depthMap.shape[1]):
        if sum_depthMap[i][j] >720:
          continue
        else:
          sum_depthMap[i][j] = (sum_depthMap[i][j]-540) * 0.005
          # print("sum_depthMap[i][j]",i, j, sum_depthMap[i][j] )

  output_sample_pts(sum_depthMap, file_name)
  return sum_depthMap




def output_sample_pts (sum_depthMap, file_name):
  sample_points = []
  cam = config.ortho_camera()


  for i in range (0, sum_depthMap.shape[0]):
    for j in range (0, sum_depthMap.shape[1]):
        if sum_depthMap[i][j] >720:
          continue
        else:
          dist = sum_depthMap[i][j]
          pos_x = j * (5.0 / 256.0)
          pos_y = 5.0 - (i * (5.0 / 256.0))
          sample_point = np.array([pos_x, pos_y, dist[0]])
          # sample_point = cam.get_position(np.array([i,j]), dist)
          sample_points.append(sample_point)

  # sample_points = rotate_samples.main_rotate(sample_points)

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


def resize_depth_map(input_array):
  input_array_shape = input_array.shape
  zoom_factor_x = 256 / input_array_shape[0]
  zoom_factor_y = 256 / input_array_shape[1]
  resized_array = zoom(input_array, (zoom_factor_x, zoom_factor_y, 1), order=1)

  return resized_array

load_depth_map()