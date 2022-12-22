
import random, pygame, math



WIDTH, HEIGHT = 1920, 1080
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)
surface = pygame.Surface(window_size)
surface.fill("Black")
surface_screen = surface.get_rect(center=(1920 // 2, 1080 // 2))

class Body(pygame.sprite.Sprite):
    
    def __init__(self, mass, radius, x_velocity, y_velocity, start_position):
        
        """Create a body with a mass, an acceleration depending on the x and y axis, a velocity depending on the x and y axis
        and a position depending on the x and y """
        
        self.radius = 1
        self.image = pygame.Surface((radius, radius))
        self.image.fill("Black")
        self.rect = self.image.get_rect(center= start_position)
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius= radius)
        
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
        self.rect.center = (round(self.x_position), round(self.y_position))
      
    def update_all(self):
        
       self.change_x_velocity(self.x_acceleration)
       self.change_y_velocity(self.y_acceleration)
       self.change_x_position(self.change_x_velocity)
       self.change_y_position(self.y_velocity)
       
       self.update_position()
        
    def gravitation_interaction(self, other : Body):
        
        GRAVITATIONAL_CONSTANT = 6.67 * 10E-11
        DELTA_TIME = 0.1
    
        
 
def main():
    
    run = True
    pygame.init()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
               
    pygame.quit()
    
if __name__ == '__main__':
    main()