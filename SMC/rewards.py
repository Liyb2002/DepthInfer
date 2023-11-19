import load_depthmap
import procedural_objects

class rewards_calculator:
    def __init__(self):
        self.sampled_points = load_depthmap.load_depth_map()

    def get_rewards(self, obj):

        lower_x = obj.position[0] - obj.scope[0]
        lower_y = obj.position[1] - obj.scope[1]
        upper_x = obj.position[0] + obj.scope[0]
        upper_y = obj.position[1] + obj.scope[1]

        lower_j = int(lower_x / (5.0 / 256.0))
        upper_j = int(upper_x / (5.0 / 256.0))

        lower_i = int((5.0 - upper_y) / (5.0 / 256.0))
        upper_i = int((5.0 - lower_y) / (5.0 / 256.0))

        lower_depth = obj.position[2] - obj.scope[2]
        upper_depth = obj.position[2] + obj.scope[2]
        
        rewards = 0

        if lower_i<0 or lower_j<0 or upper_i>256 or upper_j>256:
            return 0
            
        # print("i:", lower_i, "-", upper_i, "j:", lower_j, "-", upper_j, "depth:", lower_depth, "-", upper_depth)

        for i in range (lower_i, upper_i):
            for j in range (lower_j, upper_j):
                cur_depth = self.sampled_points[i][j]
                # print("i:", i, "j:", j, "depth:", cur_depth)

                if lower_depth <= cur_depth and cur_depth <= upper_depth:
                    self.sampled_points[i][j] = 720
                    rewards +=1 
        
        # print("rewards", rewards)
        return rewards 