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

def center_text (text):
    text_width = text.get_width()
    x_coord = (1000 - text_width)/2
    return x_coord

def find_textbox (text):
    text_width = text.get_width()
    text_height = text.get_height()
    x_coord = (1000 - text_width)/2
    y_coord = 400
    rect = pygame.Rect(x_coord, y_coord, text_width, text_height)
    return rect

Intro_Screen1 = "Welcome!"
progress = "Click anywhere to progress"
Intro_Screen2 = "This game has many levels"
Intro_Screen3 = "With many different puzzles"
Intro_Screen4 = "You will have to use your brain to solve these puzzles!"
Intro_Screen5 = "You will have to think outside the box"
Intro_Screen6 = "Now, you may start"
Intro_Screen7a = "Click"
Intro_Screen7b =  "ANYWHERE"
Intro_Screen8 = "See, you're getting it!"
Intro_Screen9 = "Go ahead"
Intro = [Intro_Screen1, Intro_Screen2, Intro_Screen3, Intro_Screen4, Intro_Screen5, Intro_Screen6, Intro_Screen7a, Intro_Screen7b, Intro_Screen8, Intro_Screen9]
progression = 0

run = True
t = Intro_Screen7b
while run:
    my_font = pygame.font.SysFont('Arial', 50)
    # INTRO
    Intro_Screen1_message = my_font.render(Intro_Screen1, True, (255, 255, 255))
    Intro_Screen2_message = my_font.render(Intro_Screen2, True, (255, 255, 255))
    Intro_Screen3_message = my_font.render(Intro_Screen3, True, (255, 255, 255))
    Intro_Screen4_message = my_font.render(Intro_Screen4, True, (255, 255, 255))
    Intro_Screen5_message = my_font.render(Intro_Screen5, True, (255, 255, 255))
    Intro_Screen6_message = my_font.render(Intro_Screen6, True, (255, 255, 255))
    Intro_Screen7a_message = my_font.render(Intro_Screen7a, True, (255, 255, 255))
    Intro_Screen7b_message = my_font.render(Intro_Screen7b, True, (255, 255, 255))
    Intro_Screen8_message = my_font.render(Intro_Screen8, True, (255, 255, 255))
    Intro_Screen9_message = my_font.render(Intro_Screen9, True, (255, 255, 255))
    Intro_list = [Intro_Screen1_message, Intro_Screen2_message, Intro_Screen3_message, Intro_Screen4_message, Intro_Screen5_message, Intro_Screen6_message, Intro_Screen7a_message, Intro_Screen7b_message, Intro_Screen8_message, Intro_Screen9_message]
    # INTRO
    b_height = Intro_Screen7b_message.get_height()
    b_width = Intro_Screen7b_message.get_width()
    b_rect = pygame.Rect(-100, -100, b_height, b_width)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        if progression < 6:
            if event.type == pygame.MOUSEBUTTONUP:
                progression += 1
                print(progression)  #DELETE LATER
        if event.type == pygame.MOUSEBUTTONUP and b_rect.collidepoint(event.pos):
            print("Maybe??!?!")



    screen.fill((50, 40, 98))
    # INTRO BLITTING
    if progression < 6:
        Current_message = Intro_list[progression]
        x = center_text(Intro_list[progression])
        screen.blit(Current_message, (x, 350))
        my_font = pygame.font.SysFont('Arial', 25)
        progress_message = my_font.render(progress, True, (255, 255, 255))
        x = center_text(progress_message)
        screen.blit(progress_message, (x, 700))

    if progression == 6:
        Current_message1 = Intro_list[6]
        x1 = center_text(Intro_list[6])
        Current_message2 = Intro_list[7]
        x2 = center_text(Intro_list[7])
        screen.blit(Current_message1, (x1, 300))
        screen.blit(Current_message2, (x2, 400))
        b_height = Intro_Screen7b_message.get_height()
        b_width = Intro_Screen7b_message.get_width()
        b_rect = pygame.Rect(x2, 400, b_height, b_width)
    pygame.display.update()



pygame.quit()