import pygame
import math

ball_position = [0, 0]
DEG2GRAD = math.pi / 180
ball_speed = 5
ball_diameter = 5
SCREEN_RES = (800, 600)
x, y = SCREEN_RES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIN = pygame.display.set_mode(SCREEN_RES)
pygame.display.set_caption("Bouncing")
FPS = 60
CENTER = [x//2 , y//2]
CENTER_SIZE = 150


def next_position(ball_position, ball_vector):

    ball_position[0] += ball_vector[0]
    ball_position[1] += ball_vector[1]


def draw_window():
    WIN.fill(BLACK)
    pygame.draw.circle(WIN, WHITE, ball_position, ball_diameter)
    pygame.draw.circle(WIN, WHITE, CENTER, CENTER_SIZE)
    pygame.display.update()


def ball_run():
    run = True
    clock = pygame.time.Clock()
    ball_vector = pygame.math.Vector2(ball_speed, ball_speed)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        impact_vector = pygame.math.Vector2(CENTER[0]-ball_position[0], CENTER[1]-ball_position[1])
        if math.dist(CENTER,ball_position) < CENTER_SIZE:
            ball_vector = ball_vector.reflect(impact_vector)
        if ball_position[0]<0:
            ball_vector = ball_vector.reflect([5,0])
        if ball_position[0] > SCREEN_RES[0]:
            ball_vector = ball_vector.reflect([-5,0])
        if ball_position[1]< 0:
            ball_vector = ball_vector.reflect([0,5])
        if ball_position[1] > SCREEN_RES[1]:
            ball_vector = ball_vector.reflect([0,-5])

        next_position(ball_position, ball_vector)

        draw_window()

    pygame.quit()


def main():
    ball_run()


if __name__ == "__main__":
    main()