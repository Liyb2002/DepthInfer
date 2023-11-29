import math 
import numpy as np
import math

PI = 3.14


class ortho_camera:
    def __init__(self):
        # Define the camera parameters
        self.camera_position = np.array([5.0, 5.0, 5.0])  # Camera position in 3D space
        self.lookat_point = np.array([0.0, 0.0, 0.0])   # Look-at point (where the camera is pointing)
        self.up_vector = np.array([0.0, 1.0, 0.0])       # Up vector for camera orientation
        self.screen_width = 256                    # Width of the screen in pixels
        self.screen_height = 256                   # Height of the screen in pixels
        self.world_width = 2.5 # Width of the world coordinates
        self.world_height = 3.0  # Height of the world coordinates

        # Calculate the direction vectors
        self.direction = self.lookat_point - self.camera_position
        self.direction /= np.linalg.norm(self.direction)
        self.right = np.cross(self.direction, self.up_vector)
        self.right /= np.linalg.norm(self.right)
        self.up = np.cross(self.right, self.direction)

        self.plane = find_plane(self.right, self.up, self.camera_position)

    def get_ray(self, x,y):
        ndc_x = (x - 128) / self.screen_width
        ndc_y = (128 - y) / self.screen_height

        # Calculate the world coordinates of the current pixel
        world_x = self.camera_position[0] + (ndc_x * self.world_width  * self.right[0]) + (ndc_y * self.world_height * self.up[0])
        world_y = self.camera_position[1] + (ndc_x * self.world_width  * self.right[1]) + (ndc_y * self.world_height * self.up[1])
        world_z = self.camera_position[2] +  (ndc_x * self.world_width  * self.right[2]) + (ndc_y * self.world_height * self.up[2])

        # Create the ray from the camera to the current pixel
        ray_origin = np.array([world_x, world_y, world_z])

        return ray_origin

    #with start world pos
    def get_intersections_withPos(self, pos_1, k):
        pos_2 = pos_1 + (k *0.25) * self.direction

        return pos_2
    
    #with start screen pos
    def get_position(self, startPos, k):
        ro = self.get_ray(startPos[0], startPos[1])
        pos = ro + k * self.direction

        return pos
    
    def get_uv(self, point):
        intersection_pt = find_intersection(self.plane, point, self.direction)
        u = (intersection_pt[0] - self.camera_position[0]) / self.right[0]
        v = (intersection_pt[1] - self.camera_position[1]) / self.up[1]

        # print("u", u, "v", v)
        return (u * self.screen_width, v * self.screen_height)


def find_plane(dir1, dir2, point):

    dir1 = dir1 / np.linalg.norm(dir1)    
    dir2 = dir2 / np.linalg.norm(dir2)    

    # Take the cross product of the direction vectors to find the normal vector of the plane
    normal_vector = np.cross(dir1, dir2)

    # Calculate the constant term in the plane equation
    constant = -np.dot(normal_vector, point)
    
    # Return the coefficients of the plane equation
    return np.append(normal_vector, constant)

def find_intersection(plane_eq, point, direction_vector):
    # Extract plane equation coefficients
    A, B, C, D = plane_eq

    # Extract point coordinates
    px, py, pz = point

    # Extract direction vector components
    dx, dy, dz = direction_vector

    # Calculate dot product
    dot_product = A * dx + B * dy + C * dz

    # Check if direction vector is parallel to the plane
    if dot_product == 0:
        print("Direction vector is parallel to the plane. No intersection point exists.")
        return None

    # Calculate parameter t
    t = - (A * px + B * py + C * pz + D) / dot_product

    # Calculate intersection point
    intersection_x = px + t * dx
    intersection_y = py + t * dy
    intersection_z = pz + t * dz

    return intersection_x, intersection_y, intersection_z
