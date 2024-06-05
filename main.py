import pygame
import random
import time
from trick1 import Mouse
from cheese import Cheese

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
Intro_Screen7b = "ANYWHERE"
Intro_Screen8 = "See, you're getting it!"
Intro_Screen9 = "Go ahead"
Intro = [Intro_Screen1, Intro_Screen2, Intro_Screen3, Intro_Screen4, Intro_Screen5, Intro_Screen6, Intro_Screen7a, Intro_Screen7b, Intro_Screen8, Intro_Screen9]
Level1_text1 = "Catch the Mouse!"
Level1_text2 = "You have to be faster than that!"
Level1_hint = "Hint: What do mice like?"
level1_hint2 = "Atleast show some excitement!"
reveal1 = "C"
reveal2 = "H"
reveal3 = "E"
reveal4 = "E"
reveal5 = "S"
reveal6 = "E"
reveal7 = "!"
reveal8 = "!"
reveal9 = "!"
move_times = 0
progression = 0
reveal = 0
collision = False
run = True
t = Intro_Screen7b
m = Mouse(300, 200)
c = Cheese(300, 600)
letter1 = False
letter2 = False
letter3 = False
letter4 = False
letter5 = False
letter6 = False
letter7 = False
letter8 = False
letter9 = False
cheese = False
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
    Level1_text1_message = my_font.render(Level1_text1, True, (255, 255, 255))
    Level1_text2_message = my_font.render(Level1_text2, True, (255, 255, 255))
    Level1_hint_message = my_font.render(Level1_hint, True, (255, 255, 255))
    reveal1_message = my_font.render(reveal1, True, (255, 255, 255))
    reveal2_message = my_font.render(reveal2, True, (255, 255, 255))
    reveal3_message = my_font.render(reveal3, True, (255, 255, 255))
    reveal4_message = my_font.render(reveal4, True, (255, 255, 255))
    reveal5_message = my_font.render(reveal5, True, (255, 255, 255))
    reveal6_message = my_font.render(reveal6, True, (255, 255, 255))
    reveal7_message = my_font.render(reveal7, True, (255, 255, 255))
    reveal8_message = my_font.render(reveal8, True, (255, 255, 255))
    reveal9_message = my_font.render(reveal9, True, (255, 255, 255))
    Level1_hint2_message = my_font.render(level1_hint2, True, (255, 255, 255))
    #######                      REMEMBER TO BLIT THE REVEAL LETTERS                    ############
    # INTRO
    b_height = Intro_Screen7b_message.get_height()
    b_width = Intro_Screen7b_message.get_width()
    b_rect = pygame.Rect(381, 400, b_width, b_height)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        pos = pygame.mouse.get_pos()
        if progression < 6 or (progression < 9 and progression > 6):
            if event.type == pygame.MOUSEBUTTONUP:
                progression += 1
                print(progression)  #DELETE LATER
        if progression == 6:
            if event.type == pygame.MOUSEBUTTONUP and b_rect.collidepoint(pos):
                progression += 1
                print("Maybe??!?!")
        if progression == 9:
            if m.rect.collidepoint(pos):
                collision = True
                message = "Collision detected"
                move_times += 1
                print(message)
                m.x = random.randint(0, 900)
                m.y = random.randint(0, 700)
                m.move(m.x, m.y)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_c]:
                letter1 = True
            if letter1 == True:
                if keys[pygame.K_h]:
                    letter2 = True
            if letter2 == True:
                if keys[pygame.K_e]:
                    letter3 = True
            if letter3 == True:
                if keys[pygame.K_e]:
                    letter4 = True
            if letter4 == True:
                if keys[pygame.K_s]:
                    letter5 = True
            if letter5 == True:
                if keys[pygame.K_e]:
                    letter6 = True
            if letter6 == True:
                if keys[pygame.K_EXCLAIM]:
                    letter7 = True
            if letter7 == True:
                if keys[pygame.K_EXCLAIM]:
                    letter8 = True
                if letter8 == True:
                    if keys[pygame.K_EXCLAIM]:
                        letter9 = True
            if letter1 == True and letter2 == True and letter3 == True and letter4 == True and letter5 == True and letter6 == True and letter7 == True and letter8 == True and letter9 == True:
                letter1 = False
                letter2 = False
                letter3 = False
                letter4 = False
                letter5 = False
                letter6 = False
                cheese = True








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

    if progression < 9 and progression > 6:
        Current_message = Intro_list[progression + 1]
        x = center_text(Intro_list[progression + 1])
        screen.blit(Current_message, (x, 350))
        my_font = pygame.font.SysFont('Arial', 25)
        progress_message = my_font.render(progress, True, (255, 255, 255))
        x = center_text(progress_message)
        screen.blit(progress_message, (x, 700))

    if progression == 9:
        screen.fill((50, 40, 98))
        screen.blit(m.image, m.rect)
        if move_times <= 10:
            x = center_text(Level1_text1_message)
            screen.blit(Level1_text1_message, (x, 20))
        if move_times > 10 and move_times <= 20:
            x = center_text(Level1_text2_message)
            screen.blit(Level1_text2_message, (x, 20))
        if move_times >20:
            x = center_text(Level1_hint_message)
            screen.blit(Level1_hint_message, (x, 20))
        keys = pygame.key.get_pressed()
        if letter1 == True:
            screen.blit(reveal1_message, (150, 700))
        if letter2 == True:
            screen.blit(reveal2_message, (250, 700))
        if letter3 == True:
            screen.blit(reveal3_message, (350, 700))
        if letter4 == True:
            screen.blit(reveal4_message, (450, 700))
        if letter5 == True:
            screen.blit(reveal5_message, (550, 700))
        if letter6 == True:
            screen.blit(reveal6_message, (650, 700))
        if cheese == True:
            screen.blit(c.image, c.rect)


    pygame.display.update()



pygame.quit()