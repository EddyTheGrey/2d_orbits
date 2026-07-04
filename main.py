import numpy as np
from points import Body
from matrix import create_matrix, update_matrix
from grid import create_grid


def create_bodies(num_bodies):
    """Creates a list of Body objects with random initial conditions."""
    bodies = []
    for _ in range(num_bodies):
        mass = 1.0  # You can randomize this if needed
        x = 0.0     # You can randomize this if needed
        y = 0.0     # You can randomize this if needed
        vx = 0.0    # You can randomize this if needed
        vy = 0.0    # You can randomize this if needed
        bodies.append(Body(mass, x, y, vx, vy))
    return bodies
