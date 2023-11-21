import random
import load_depthmap
import class_dummy_object
import class_particle
from copy import deepcopy

class data_gen:
    def __init__(self):
        self.num_particles = 500


    def prepare_pariticle(self):
        #will return a particle at a random stage
        _, vb = load_depthmap.load_depth_map()
        start_obj = class_dummy_object.dummy_object(np.array([vb[0], vb[1], vb[2]]), np.array([0.1,0.1,0.1]))
        particle_list = []

        for i in range(self.num_particles):
            tempt_particle = class_particle.Particle(start_obj, deepcopy(self.rewards_calculator))
            particle_list.append(tempt_particle)

        step = 0
        final_step = random.randint(2, 20)
        highest_hit_particle = None

        while(step < final_step):
            step += 1
            print("step", step)
            for i in range(self.num_particles):
                tempt_particle = particle_list[i]
                tempt_particle.run_step()
                # print("tempt_particle.score", tempt_particle.score)
            
            particle_list = resample.resample(particle_list)   
            highest_hit_particle = max(particle_list, key=lambda p: p.hit)


        return highest_hit_particle
    

    def get_choices(self, highest_hit_particle):
        #the input is a single particle, the output is the prob the current stage make a choice. 

        particle_list = []
        for i in range(self.num_particles):
            tempt_particle = deepcopy(highest_hit_particle)
            tempt_particle.run_step()
            particle_list.append(tempt_particle)

        particle_list = resample.resample(particle_list)   

        choices = []
        for i in range (self.num_particles):
            tempt_particle = particle_list[i]
            new_obj = tempt_particle.procedural_objects[-1]
            
            #what to write???

