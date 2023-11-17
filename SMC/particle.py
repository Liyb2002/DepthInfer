import produce
import procedural_objects
import numpy as np
import math

class Particle:
    def __init__(self, generic_object_list):
        self.generic_object_list = generic_object_list
        self.procedural_objects = []

    def prepare_particle(self,intersection, start_type, connected_dir):
        self.cur_obj = start_obj(intersection, self.generic_object_list, start_type, connected_dir)
        self.procedural_objects.append(self.cur_obj)

    def run_step(self):
        self.procedural_objects = produce.execute_model(self.generic_object_list, self.cur_obj, 5)





def start_obj(start_pos, generic_object_list, start_type, connected_dir):

    cur_type = start_type
    start_scope = generic_object_list[cur_type].scope
    gen_hash = generic_object_list[cur_type].generate_hash()
    next_rotation = generic_object_list[cur_type].rotation
    cur_obj = procedural_objects.Procedural_object(cur_type, start_pos, start_scope, gen_hash,next_rotation, np.array([0,0,0]))
    cur_obj_x = cur_obj.length[0]
    cur_obj_y = cur_obj.length[1]
    cur_obj_z = cur_obj.length[2]
    update_pos = np.array([cur_obj_x, cur_obj_y, cur_obj_z])
    cur_obj.arbitrary_set_position(start_pos - update_pos)
    cur_obj.add_connected(connected_dir)

    return cur_obj

