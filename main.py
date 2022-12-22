import random, pygame, math, itertools
from numba import *


WIDTH, HEIGHT = 1920, 1080
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)
surface = pygame.Surface(window_size)
surface.fill("Black")
surface_screen = surface.get_rect(center=(1920 // 2, 1080 // 2))
DELTA_TIME = 0.2

class Body(pygame.sprite.Sprite):
    
    def __init__(self, mass, radius, x_velocity, y_velocity, start_position, color):
        
        super().__init__()
        
        """Create a body with a mass, an acceleration depending on the x and y axis, a velocity depending on the x and y axis
        and a position depending on the x and y """
        
        self.radius = 1
        self.color = color
        self.image = pygame.Surface((radius, radius))
        self.image.fill("Black")
        self.rect = self.image.get_rect(center= start_position)
        pygame.draw.circle(self.image, color, (radius, radius), radius= radius)
        
        self.mass = mass
        self.x_acceleration = 0
        self.y_acceleration = 0
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.x_position = start_position[0]
        self.y_position = start_position[1]
        
    #Method to change acceleration depending on the axis 
    
    def set_x_acceleration(self, x_acceleration):
        self.x_acceleration = x_acceleration
        
    def set_y_acceleration(self, y_acceleration):
        self.y_acceleration = y_acceleration
    
    #Method to change velocity depending on the axis 
    
    def set_x_velocity(self, x_velocity):
        self.x_velocity = x_velocity
        
    def set_y_velocity(self, y_velocity):
        self.y_velocity = y_velocity
        
    #Method to change position depending on the axis 
     
    def set_x_position(self, x_position):
        self.x_position = x_position
    
    def set_x_position(self, x_position):
        self.x_position = x_position
        
    def change_x_velocity(self, value):
        self.x_velocity += value
    
    def change_y_velocity(self, value):
        self.y_velocity += value
        
    def change_x_position(self, value):
        self.x_position += value
        
    def change_y_position(self, value):
        self.y_position += value
        
    def update_position(self):
        
        if self.color != (255, 255, 255):
            pass
        
        else:
            if self.x_position <= 0:
                self.change_x_position(0)
                
            elif self.x_position >= WIDTH:
                self.change_x_position(WIDTH)
                
            if self.y_position <= 0:
                self.change_y_position(0)
                
            elif self.y_position >= HEIGHT:
                self.change_y_position(HEIGHT)
        
            self.rect.center = (round(self.x_position), round(self.y_position))
      
    def update_all(self):
        
       self.change_x_velocity(self.x_acceleration * DELTA_TIME)
       self.change_y_velocity(self.y_acceleration * DELTA_TIME)
       self.change_x_position(self.x_velocity * DELTA_TIME)
       self.change_y_position(self.y_velocity * DELTA_TIME)
       print(self.x_acceleration, self.y_acceleration)
       
       self.update_position()
       
    def gravitation_interaction(self, other):
        
        """Change the acceleration of self when there's a gravitational interaction with another body"""
            
        GRAVITATIONAL_CONSTANT = 1
            
        distance_x = abs(self.x_position - other.x_position)
        distance_y = abs(self.y_position - other.y_position)
        
        if distance_x < self.radius * 2 and distance_y < self.radius * 2:
            pass
        
        else:
            try:
                r = math.sqrt(distance_x ** 2 + distance_y ** 2)
                theta = math.asin(distance_y / r)
                a = GRAVITATIONAL_CONSTANT * other.mass / r ** 2

                if self.x_position >= other.x_position:
                    self.set_x_acceleration(a * -math.cos(theta))
                else:
                    self.set_x_acceleration(a * math.cos(theta))
                
                if self.y_position >= other.y_position:
                    self.set_y_acceleration(a * -math.sin(theta))
                else:
                    self.set_y_acceleration(a * math.sin(theta))
                        
            except ZeroDivisionError:
                pass

class Galaxy():
    
    def __init__(self, diameter):
        self.diameter = diameter
        self.center_x = 1920 // 2
        self.center_y = 1080 // 2
        self.center = Body
        self.all_bodies = pygame.sprite.Group()
        self.list_body = list(self.all_bodies)
        self.iterable_list = list(itertools.combinations(self.list_body, 2))

    def add_body(self, n):
        
        self.center = Body(n / 3, 5, 0, 0, (self.center_x, self.center_y), (255, 255, 0))
        self.all_bodies.add(self.center)
        
        for i in range(n):
            x_position = random.randint(0, 1920)
            y_position = random.randint(0, 1080)
            distance = math.sqrt((x_position - self.center_x) ** 2 + (y_position - self.center_y) ** 2)
            
            while distance >= self.diameter // 2:   
                x_position = random.randint(0, 1920)
                y_position = random.randint(0, 1080)
                distance = math.sqrt((x_position - self.center_x) ** 2 + (y_position - self.center_y) ** 2)
                
            self.all_bodies.add(Body(1, 1, 0, 0, (x_position, y_position), (255, 255, 255))) 
        
          

N_BODIES = 1
color_list = (((255,0,0), (255, 255, 0), (255, 255, 255), (0, 0, 255)))
 
def main():
    
    run = True
    pygame.init()
    galaxy = Galaxy(200)
    galaxy.add_body(N_BODIES)
    all_bodies = galaxy.all_bodies
    list_body = list(all_bodies)
    iterable_list = list(itertools.combinations(list_body, 2))

    while run:
        
        screen.fill("Black")
        galaxy.all_bodies.draw(screen)
        
        for body, other in iterable_list:
            body.gravitation_interaction(other)
            other.gravitation_interaction(body)
            body.update_all()
            other.update_all()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

               
    pygame.quit()
    
if __name__ == '__main__':
    main()