import numpy as np
import random, pygame, math
from Body import Body


WIDTH, HEIGHT = 1920, 1080
window_size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(window_size)

n = 10

positions = np.zeros((n, n))
velocities = np.zeros((n, n))
masses = np.zeros(n)
acceleration = np.zeros((n, n))

for i in range(n):
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        m = random.randint(1 * 10E5, 10 * 10E5)
        positions[i, 0] = x
        positions[i, 1] = y
        masses[i] = m
        
def n_bodies(n):
    
    delta_time = 0.01
    G = 6.67 * 10E-11
    
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = np.linalg.norm(positions[j] - positions[i])
                acceleration[i] += masses[j] / distance ** 3
            velocities[i] += acceleration[i] * delta_time
            positions[i] += velocities[i] * delta_time
            
            #Making sure that the bodies aren't going out of the screen
            
            positions[positions < 0] = 0
            positions[positions > WIDTH] = WIDTH
            positions[:, 1][positions[:, 1] < 0] = 0
            positions[:, 1][positions[:, 1] > HEIGHT] = HEIGHT
            
    return positions

def draw_bodies():
    
    screen.fill(color=(0,0,0))
    
    for i in range(n):
        x = positions[i, 0]
        y = positions[i, 1]
        pygame.draw.circle(screen, (255, 255, 255), (int(x), int(y)), 1)
 
def main():
    
    run = True
    pygame.init()
    
    while run:
        
        draw_bodies()
        n_bodies(n)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
               
    pygame.quit()
    
if __name__ == '__main__':
    main()