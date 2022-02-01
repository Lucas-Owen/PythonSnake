width = 700
height = 400
from pygame import draw
class Segment():
    def __init__(self, x, y, direction = "right"):
        self.x = x
        self.y = y
        self.width = 10
        self.velocity = self.width + 1
        self.framerate = 9
        self.direction = direction
        self.n = 0

    def draw(self, window):
        draw.rect(window, (0, 200, 0), (self.x, self.y, self.width, self.width))

    def turn(self, snake):
        for turning_point in snake.turning_points:
            if (self.x, self.y) == (turning_point[0], turning_point[1]):
                self.direction = turning_point[2]
                turning_point[3][0] += 1
                if turning_point[3][0] == len(snake.segments):
                    snake.turning_points.remove(turning_point)
                break

    def move(self):
        if self.direction == "left":
            self.x -= self.velocity
            if self.x < 0:
                self.x = width - self.width
        if self.direction == "right":
            self.x += self.velocity
            if self.x > width:
                self.x = 0
        if self.direction == "up":
            self.y -= self.velocity
            if self.y < 0:
                self.y = height - self.width
        if self.direction == "down":
            self.y += self.velocity
            if self.y > height:
                self.y = 2
