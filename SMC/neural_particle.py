import create_dummy
import procedural_objects
import numpy as np
import math

import model

class Particle:
    def __init__(self, start_obj, rewards_calculator, target_pts):
        self.procedural_objects = []
        self.procedural_objects.append(start_obj)
        self.rewards_calculator = rewards_calculator
        self.target_pts = target_pts

        self.hit = 0
        self.score = 0

    def run_step(self):
        prediction = model.make_prediction(self.target_pts, self.procedural_objects)
        new_obj = create_dummy.create_target_dummy(self.procedural_objects[-1], prediction)

        self.calc_score(new_obj)
        self.check_collision(new_obj)
        self.procedural_objects.append(new_obj)


    def calc_score(self, new_obj):
        reward = self.rewards_calculator.get_rewards(new_obj)
        self.hit += reward
        self.score = 0.5 * self.score + reward * reward

        if reward < 3:
            self.score = 0
        


    def check_collision(self, new_object):
        new_aabb = new_object.get_aabb()
        for obj in self.procedural_objects:
            obj_aabb = obj.get_aabb()
            if (new_aabb["min_x"] <= obj_aabb["max_x"] and
                new_aabb["max_x"] >= obj_aabb["min_x"] and
                new_aabb["min_y"] <= obj_aabb["max_y"] and
                new_aabb["max_y"] >= obj_aabb["min_y"] and
                new_aabb["min_z"] <= obj_aabb["max_z"] and
                new_aabb["max_z"] >= obj_aabb["min_z"]):

                self.score = 0
        
        


