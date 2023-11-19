from copy import deepcopy
import random

def resample(particle_list):
    total_score = 1 + sum(particle.score for particle in particle_list)

    probabilities = [particle.score / total_score for particle in particle_list]

    new_particles = random.choices(particle_list, weights=probabilities, k=len(particle_list))

    return new_particles
