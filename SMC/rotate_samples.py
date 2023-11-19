import numpy as np
from scipy.spatial.transform import Rotation as R

def rotation_matrix_from_vectors(vec1, vec2):
    """ Find the rotation matrix that aligns vec1 to vec2 """
    a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (vec2 / np.linalg.norm(vec2)).reshape(3)
    v = np.cross(a, b)
    c = np.dot(a, b)
    s = np.linalg.norm(v)
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))
    return rotation_matrix


def main_rotate(point_cloud):
    original_view_vector = np.array([0, 0, 5]) - np.array([5, 5, 5])
    new_view_vector = np.array([5, 5, 5]) - np.array([5, 5, 5])

    # Calculate the rotation matrix
    rot_matrix = rotation_matrix_from_vectors(original_view_vector, new_view_vector)


    # Apply the rotation to each point
    rotated_point_cloud = np.dot(point_cloud, rot_matrix.T)

    return rotated_point_cloud