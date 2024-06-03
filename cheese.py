import pygame


class Cheese:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("cheese.png")
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .2

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .1, self.image_size[1] * .1)
        self.image = pygame.transform.scale(self.image, scale_size)
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])