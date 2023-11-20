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
  smallest_element = smallest_element - 5
  
  for i in range (0, sum_depthMap.shape[0]):
    for j in range (0, sum_depthMap.shape[1]):
        if sum_depthMap[i][j] >720:
          continue
        else:
          sum_depthMap[i][j] = (sum_depthMap[i][j]-smallest_element) * 0.02

  # sample_points = output_sample_pts(sum_depthMap, file_name)
  sample_points = nonWriting_sample_pts(sum_depthMap, file_name)
  vb = find_vb(sample_points)
  return sum_depthMap, vb


def nonWriting_sample_pts (sum_depthMap, file_name):
  sample_points = []

  for i in range (0, sum_depthMap.shape[0]):
    for j in range (0, sum_depthMap.shape[1]):
        if sum_depthMap[i][j] >720:
          continue
        else:
          dist = sum_depthMap[i][j]
          pos_x = j * (5.0 / 256.0)
          pos_y = 5.0 - (i * (5.0 / 256.0))
          sample_point = np.array([pos_x, pos_y, dist[0]])
          sample_points.append(sample_point)
    
  return sample_points


def output_sample_pts (sum_depthMap, file_name):
  sample_points = []


  for i in range (0, sum_depthMap.shape[0]):
    for j in range (0, sum_depthMap.shape[1]):
        if sum_depthMap[i][j] >720:
          continue
        else:
          dist = sum_depthMap[i][j]
          pos_x = j * (5.0 / 256.0)
          pos_y = 5.0 - (i * (5.0 / 256.0))
          sample_point = np.array([pos_x, pos_y, dist[0]])
          sample_points.append(sample_point)

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
    
  return sample_points


def resize_depth_map(input_array):
  input_array_shape = input_array.shape
  zoom_factor_x = 256 / input_array_shape[0]
  zoom_factor_y = 256 / input_array_shape[1]
  resized_array = zoom(input_array, (zoom_factor_x, zoom_factor_y, 1), order=1)

  return resized_array


def find_vb(sample_points):
  max_diff = 0
  vb = [0,0,0]
  for i in range (1, len(sample_points)):
    diff = sample_points[i][2] - sample_points[i-1][2]
    if diff > max_diff:
      max_diff = diff
      vb = sample_points[i-1]
  
  return vb

