
import class_particle
import load_depthmap
import rewards
import resample

from copy import deepcopy
import numpy as np

class generate_helper:
    def __init__(self, generic_object_list, visual_bridge_info):
        #find impossible intersection positions

        self.generic_object_list = generic_object_list
        self.visual_bridge_info = visual_bridge_info
        self.particle_list = []
        self.rewards_calculator = rewards.rewards_calculator()


    def smc_process(self):
        
        num_particles = 100
        start_pos = np.array([1.11328125, 4.1015625, 2.4])

        start_type = 1
        connected_dir = ''

        for i in range(num_particles):
            tempt_particle = class_particle.Particle(self.generic_object_list, self.rewards_calculator)
            tempt_particle.prepare_particle(start_pos, start_type, connected_dir)
            self.particle_list.append(tempt_particle)

        for i in range (10):
            print("step", i)
            for tempt_particle in self.particle_list:
                tempt_particle.run_step()
                tempt_particle.calc_score()
                # print("tempt_particle.score", tempt_particle.score)
            
            self.particle_list = resample.resample(self.particle_list)   

        
        highest_score_particle = max(self.particle_list, key=lambda p: p.score)
        return highest_score_particle.procedural_objects

