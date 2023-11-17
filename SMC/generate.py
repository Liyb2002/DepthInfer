
import particle

from copy import deepcopy
import numpy as np

class generate_helper:
    def __init__(self, generic_object_list, visual_bridge_info):
        #find impossible intersection positions

        self.generic_object_list = generic_object_list
        self.visual_bridge_info = visual_bridge_info
        self.particle_list = []



    def smc_process(self):
        
        num_particles = 10
        start_pos = np.array([1, 1, 1])
        start_type = 1
        connected_dir = '-x'

        for i in range(num_particles):
            tempt_particle = particle.Particle(self.generic_object_list)
            tempt_particle.prepare_particle(start_pos, start_type, connected_dir)
            self.particle_list.append(tempt_particle)

        
        for i in range(len(self.particle_list)):
            tempt_particle = self.particle_list[i]
            tempt_particle.run_step()     

        return self.particle_list[0]

