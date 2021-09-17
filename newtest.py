import pygame
import test
display = pygame.display.set_mode((600, 600))
background = pygame.image.load('pictures/background.png')
while True:
    display.blit(background, (0, 0))
    rect = pygame.draw.rect(display, (255, 0, 0), (270, 300, 100, 40))
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        break
    pygame.display.update()
