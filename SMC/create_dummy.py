import class_dummy_object
import random
import numpy as np

def create_dummy_object(cur_dummy_obj):
    pos_offset = np.array([random_offset(), random_offset(), random_offset()])
    new_obj = class_dummy_object.dummy_object(cur_dummy_obj.position + pos_offset, cur_dummy_obj.scope)
    return new_obj

def random_offset():
    if random.random() < 0.5:
        return np.random.uniform(-0.2, -0.1)

    return np.random.uniform(0.1, 0.2)   

def create_target_dummy(cur_dummy_obj, next_pos):
    new_obj = class_dummy_object.dummy_object(cur_dummy_obj.position + next_pos, cur_dummy_obj.scope)
    return new_obj