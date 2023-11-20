
import class_particle
import load_depthmap
import rewards
import resample

import class_dummy_object

from copy import deepcopy
import numpy as np
from copy import deepcopy

class generate_helper:
    def __init__(self, generic_object_list, visual_bridge_info):
        #find impossible intersection positions

        self.generic_object_list = generic_object_list
        self.visual_bridge_info = visual_bridge_info
        self.particle_list = []
        self.rewards_calculator = rewards.rewards_calculator()


    def smc_process(self):

        num_particles = 500
        _, vb = load_depthmap.load_depth_map()
        start_obj = class_dummy_object.dummy_object(np.array([vb[0], vb[1], vb[2]]), np.array([0.1,0.1,0.1]))

        for i in range(num_particles):
            tempt_particle = class_particle.Particle(start_obj, deepcopy(self.rewards_calculator))
            self.particle_list.append(tempt_particle)

        step = 0
        while(True):
            step += 1
            print("step", step)
            for i in range(num_particles):
                tempt_particle = self.particle_list[i]
                tempt_particle.run_step()
                # print("tempt_particle.score", tempt_particle.score)
            
            self.particle_list = resample.resample(self.particle_list)   
            highest_hit_particle = max(self.particle_list, key=lambda p: p.hit)
            print("highest hit", highest_hit_particle.hit)
            if highest_hit_particle.hit > 5500:
                break
        

        highest_hit_particle = max(self.particle_list, key=lambda p: p.hit)

        return highest_hit_particle.procedural_objects

