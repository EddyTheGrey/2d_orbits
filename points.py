

class Body:
    def __init__(self, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update_position(self, dt):
        """Updates the position of the body based on its velocity and the time step."""
        self.x += self.vx * dt
        self.y += self.vy * dt
    def update_velocity(self, ax, ay, dt):
        """Updates the velocity of the body based on the acceleration and the time step."""
        self.vx += ax * dt
        self.vy += ay * dt