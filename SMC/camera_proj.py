import numpy as np

class Camera:
    def __init__(self):
        # Camera parameters
        self.lookfrom = np.array([5.0, 5.0, 5.0])
        self.lookat = np.array([0.0, 0.0, 0.0])
        self.vup = np.array([0.0, 1.0, 0.0])
        self.fov = 60
        self.aspect_ratio = 1.0

        self.cam_lower_left_corner = np.zeros(3)
        self.cam_horizontal = np.zeros(3)
        self.cam_vertical = np.zeros(3)
        self.cam_origin = np.zeros(3)

        self.reset()

    def reset(self):
        theta = self.fov * (3.141 / 180.0)
        half_height = 5.0
        half_width = 5.0

        self.cam_origin = self.lookfrom
        w = self.normalize(self.lookfrom - self.lookat)
        u = self.normalize(np.cross(self.vup, w))
        v = np.cross(w, u)

        self.cam_lower_left_corner = self.cam_origin - half_width * u - half_height * v - w
        self.cam_horizontal = 2 * half_width * u
        self.cam_vertical = 2 * half_height * v

    def get_ray(self, u, v):
        print("self.cam_horizontal", self.cam_horizontal, "self.cam_vertical", self.cam_vertical)
        return self.cam_lower_left_corner + u * self.cam_horizontal + v * self.cam_vertical - self.cam_origin
    
    def get_camera_origin(self):
        return self.cam_origin
    
    def get_point_on_ray(self,i , j, d):
        width = 256
        height = 256

        # Normalize pixel coordinates [i, j]
        u = (i / (width )) * 5.0
        v = ((256 - j) / (height)) * 5.0


        # Get the ray direction
        ray_direction = self.get_ray(u, v)
        ray_direction = self.normalize(ray_direction)

        # print("ray_direction", ray_direction, "d", d)

        # Calculate the 3D point at distance d along the ray
        point_3D = self.get_camera_origin() + d * ray_direction

        return point_3D

    
    def normalize(self, vec):
        norm = np.linalg.norm(vec)
        if norm == 0: 
            return vec
        return vec / norm
