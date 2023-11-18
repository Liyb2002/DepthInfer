import load_depthmap
import procedural_objects

class rewards_calculator:
    def __init__(self):
        self.sampled_points = load_depthmap.load_depth_map()

    def get_rewards(obj):

        lower_x = obj.position[0] - obj.length[0]
        lower_y = obj.position[1] - obj.length[1]
        upper_x = obj.position[0] + obj.length[0]
        upper_y = obj.position[1] + obj.length[1]

        lower_j = int(lower_x / (5.0 / 256.0))
        lower_i = int((5.0 - lower_y) / (5.0 / 256.0))
        upper_j = int(upper_x / (5.0 / 256.0))
        upper_i = int((5.0 - upper_y) / (5.0 / 256.0))

        lower_depth = obj.position[2] - obj.length[2]
        upper_depth = obj.position[2] + obj.length[2]
        
        rewards = 0

        for i in range (lower_i, upper_i):
            for j in range (lower_j, upper_j):
                cur_depth = self.sampled_points [i][j] 
                if lower_depth <= cur_depth and cur_depth <= upper_depth:
                    rewards +=1 
        
        return rewards