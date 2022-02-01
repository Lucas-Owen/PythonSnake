from segment import Segment, width, height
from random import randint
import pygame

class Snake(Segment):
    #initialize the snake at a random position on the display
    def __init__(self, segments = [Segment(randint(0, width), randint(0, height))]):
        self.segments = segments
        self.turning_points = list()
        self.grow()
        self.grow()

    def draw(self, window):
        window.fill((0, 0, 40))
        for segment in self.segments:
            segment.draw(window)

    def move(self):
        for segment in self.segments:
            if self.turning_points:
                segment.turn(self)
            segment.move()

    def check_key(self, keys):
        if keys[pygame.K_LEFT] and self.segments[0].direction != "right":
            if self.segments[0].direction == "left":
                return
            self.segments[0].direction = "left"
            self.turning_points.append((self.segments[0].x, self.segments[0].y, self.segments[0].direction, [0]))
        elif keys[pygame.K_RIGHT] and self.segments[0].direction != "left":
            if self.segments[0].direction == "right":
                return
            self.segments[0].direction = "right"
            self.turning_points.append((self.segments[0].x, self.segments[0].y, self.segments[0].direction, [0]))
        elif keys[pygame.K_UP] and self.segments[0].direction != "down":
            if self.segments[0].direction == "up":
                return
            self.segments[0].direction = "up"
            self.turning_points.append((self.segments[0].x, self.segments[0].y, self.segments[0].direction, [0]))
        elif keys[pygame.K_DOWN] and self.segments[0].direction != "up":
            if self.segments[0].direction == "down":
                return
            self.segments[0].direction = "down"
            self.turning_points.append((self.segments[0].x, self.segments[0].y, self.segments[0].direction, [0]))

    def suicide(self, window, font):
        #checks if the snake bit itself
        for i in range(3, len(self.segments)):
            if abs(self.segments[i].x - self.segments[0].x) < self.segments[0].width and abs(self.segments[i].y - self.segments[0].y) < self.segments[0].width:
                warning = font.render("GAME OVER, SUCKER!", 1, (255, 0, 0))
                window.blit(warning, (width//2 - warning.get_width()//2, 20))
                pygame.display.update() 
                pygame.time.delay(2000)
                return True
        else:
            return False

    def grow(self):
        if self.segments[-1].direction == "right":
            self.segments.append(Segment(self.segments[-1].x - self.segments[-1].width - 1, self.segments[-1].y, "right"))
        if self.segments[-1].direction == "left":
            self.segments.append(Segment(self.segments[-1].x + self.segments[-1].width + 1, self.segments[-1].y, "left"))
        if self.segments[-1].direction == "up":
            self.segments.append(Segment(self.segments[-1].x, self.segments[-1].y + self.segments[-1].width + 1, "up"))
        if self.segments[-1].direction == "down":
            self.segments.append(Segment(self.segments[-1].x, self.segments[-1].y - self.segments[-1].width - 1, "down"))