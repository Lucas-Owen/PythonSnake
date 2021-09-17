from food import Food
from snake import Snake, width, height
import pygame

window = pygame.display.set_mode((width, height))
pygame.font.init()
font = pygame.font.SysFont(pygame.font.get_default_font(), 30, True, False)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snake = Snake()
score = 0
food = Food(width, height)



Flag = True
# Sound = pygame.mixer.Sound('')
# Sound.play()
while Flag:
    clock.tick(snake.segments[0].framerate)

    snake.draw(window)
    food.draw(window)

    text = font.render("SCORE: " + str(score), 1, (100, 100, 100))
    window.blit(text, (width - text.get_width(), 4)) 
    pygame.display.update()

    snake.check_key(pygame.key.get_pressed())
    snake.move()

    if snake.suicide(window, font):
        Flag = False

    if food.eaten(snake):
        snake.grow()
        score += 1
        food = Food(width, height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Flag = False