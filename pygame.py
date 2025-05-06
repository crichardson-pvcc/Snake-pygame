import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], 10, 10])

def game_loop():
    x = 300
    y = 200
    dx = 0
    dy = 0
    snake = []
    length = 1
    foodx = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, 400 - 10) / 10.0) * 10.0
    score = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -10
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = 10
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dy = -10
                    dx = 0
                elif event.key == pygame.K_DOWN and dy == 0:
                    dy = 10
                    dx = 0
        x += dx
        y += dy
        if x >= 600 or x < 0 or y >= 400 or y < 0:
            run = False
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, 10, 10])
        head = [x, y]
        snake.append(head)
        if len(snake) > length:
            del snake[0]
        for segment in snake[:-1]:
            if segment == head:
                run = False
        draw_snake(snake)
        text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(text, [0, 0])
        pygame.display.update()
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, 600 - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, 400 - 10) / 10.0) * 10.0
            length += 1
            score += 1
        clock.tick(15)
    pygame.quit()
game_loop()
