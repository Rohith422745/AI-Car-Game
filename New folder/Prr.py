# pygame pr - 1 Basic Movements and key presses 
import pygame 
pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption('pr1')

x = 50  
y = 50
width = 60
vel = 2
height = 40     

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT]:
       x -= vel
    if keys [pygame.K_RIGHT]:
       x += vel
    

    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()
pygame.quit()

