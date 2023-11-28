import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate, Lambda
from tensorflow.keras.models import Model
import numpy as np

import load_depthmap

def make_prediction(sampled_points, geometry_list):
    process_inputs(sampled_points, geometry_list, geometry_list[-1])

    return np.array([-1,-1,-1])

def process_inputs(sampled_points, geometry_list, last_geometry, dist = [0.1, 0.2]):

    sampled_points, _ = load_depthmap.load_depth_map()
    last_x = last_geometry.position[0]
    last_y = last_geometry.position[1]
    last_x_TwoD = int(last_x / (5.0 / 256.0))
    last_y_TwoD = int((5.0 - last_y) / (5.0 / 256.0))

    lower_bound_dist = int(dist[0] / (5.0 / 256.0))
    upper_bound_dist = int(dist[1] / (5.0 / 256.0))

    smaller_z = last_geometry.position[2] - dist[1]
    larger_z = last_geometry.position[2] + dist[1]
    
    # print("z", last_geometry.position[2], "smaller_z", smaller_z, "larger_z", larger_z)

    points = []
    for i in range(lower_bound_dist, upper_bound_dist):
        possible_pts = [[last_x_TwoD + i, last_y_TwoD + i], [last_x_TwoD - i, last_y_TwoD + i], [last_x_TwoD + i, last_y_TwoD - i], [last_x_TwoD - i, last_y_TwoD - i]]

        for pt in possible_pts:
            # print("pt", pt, "value", sampled_points[pt[0]][pt[1]])
            if sampled_points[pt[0]][pt[1]] > smaller_z and sampled_points[pt[0]][pt[1]] < larger_z:
                points.append(pt)
    
    print("len", len(points))
    