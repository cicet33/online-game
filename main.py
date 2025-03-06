import pygame
import os
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('online game')
clock = pygame.time.Clock()
image_choose = input("choose the image: ")
image = str(image_choose + ".jpg")
surface = pygame.image.load(f"graphics/{image}")

   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(surface,(100,100))
    pygame.display.update()
    clock.tick(60)