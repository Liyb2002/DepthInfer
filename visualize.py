import cv2 
import random
import numpy as np

def visualize_ds(visualize_samples, num_samples = 5):

    image, depth = visualize_samples
    generic_image_filename = './vis/image'
    generic_depth_filename = './vis/depth'


    for i in range(num_samples):
        index = random.randint(0, len(depth)-1)

        image_filename = generic_image_filename + '_' + str(index) + '.png'
        depth_filename = generic_depth_filename + '_' + str(index) + '.png'

        cv2.imwrite(image_filename, image[index]*255.0) 
        cv2.imwrite(depth_filename, depth[index]*255.0) 

def visualize_result(result):
    result = result[0, :, :, :]
    result = np.repeat(result, 3, axis=2)

    print("result.shape", result.shape)
    
    filename = './vis/predict.png'
    cv2.imwrite(filename, result*255.0) 
