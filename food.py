from random import randint
import pygame
class Food():
    def __init__(self, width, height):
        self.q = randint(6, width - 11)
        self.r = randint(6, height - 11)
        self.x = self.q - self.q % 11 + 11
        self.y = self.r - self.r % 11 + 11

    def draw(self, window):
        pygame.draw.circle(window, (255, 0, 0), (self.x, self.y), 5)

    def eaten(self, snake):
        return ((self.x in range(snake.segments[0].x, snake.segments[0].x + snake.segments[0].width)) and (self.y in range(snake.segments[0].y, snake.segments[0].y + snake.segments[0].width)))