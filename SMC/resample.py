from copy import deepcopy
import random

def resample(particle_list):
    total_score = 1 + sum(particle.score for particle in particle_list)

    probabilities = [particle.score / total_score for particle in particle_list]

    selected_particles = random.choices(particle_list, weights=probabilities, k=len(particle_list))

    new_particles = [deepcopy(particle) for particle in selected_particles]

    return new_particles
