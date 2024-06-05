import pygame 
pygame.init()

win = pygame.display.set_mode((1244,1016))

pygame.display.set_caption('Self Driving car')

Track = pygame.image.load('track.png')
Car = pygame.image.load('car.png')

win.blit(Track,(0,0))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

   
    pygame.display.update()
    
pygame.quit()