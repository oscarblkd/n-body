import Body, math

class Body():
      
    def __init__(self, mass, x_position, y_position, x_velocity, y_velocity, acceleration):
        
        """Create a body with a position, a velocity, an acceleration and a force"""
        
        self.mass = mass
        self.position = (x_position, y_position)
        self.velocity = (x_velocity, y_velocity)
        self.acceleration = acceleration
        
    def distance(self, other):
        
        """Return the distance between two body"""
        
        return math.sqrt((other.position[0] - self.position[0])**2 + 
                         (other.position[1] - self.position[1])**2)
    
    def update(self, other : Body):
        
        DELTA_TIME = 0.1  
        
        """Update the acceleration of itself"""
        
        self.acceleration = 6.67 * 10E-11 * other.mass / (self.distance(other) ** 3 + 0.0000001)
        
        """Update the velocity of itself""" 
    
        self.velocity = (self.velocity[0] + self.acceleration * DELTA_TIME, self.velocity[1] + self.acceleration * DELTA_TIME)
        
        """Update the postion of the body in space"""
        
        self.position = (self.position[0] + self.velocity[0] * DELTA_TIME, self.position[1] + self.velocity[1] * DELTA_TIME)
    