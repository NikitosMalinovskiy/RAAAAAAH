import pygame
import random
import time

pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Best Project")

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

Intro_Screen1 = "Welcome!"
progress = "Click anywhere to progress"
Intro_Screen2 = "This game has many levels"
Intro_Screen3 = "With many different puzzles"
Intro_Screen4 = "You will have to use your brain to solve these puzzles!"
Intro_Screen5 = "You will have to think outside the box"
Intro_Screen6 = "Now, you may start"
Intro_Screen7 = "Click ANYWHERE"
Intro_Screen8 = "See, you're getting it!"
Intro_Screen9 = "Go ahead"
Intro = [Intro_Screen1, Intro_Screen2, Intro_Screen3, Intro_Screen4, Intro_Screen5, Intro_Screen6, Intro_Screen7, Intro_Screen8, Intro_Screen9]
progression = 0

run = True

while run:
    my_font = pygame.font.SysFont('Arial', 15)
    # INTRO
    Intro_Screen1_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen2_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen3_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen4_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen5_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen6_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen7_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen8_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen9_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    # INTRO
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if progression < 7:
            if event.type == pygame.MOUSEBUTTONUP:
                progression += 1
                print(progression)

    screen.fill((50, 40, 98))
    if progression < 7:
        for item in Intro:
            screen.blit(item, (0, 0))
    pygame.display.update()


pygame.quit()