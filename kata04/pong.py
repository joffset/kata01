import pygame


screen_width = 1280
screen_height = 960

back_color = (200, 200, 200)
light_gray = pygame.Color('grey112')

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((screen_width, screen_height))

def mover_rectangulo():
    rectangulo.top +=1
    if rectangulo.top + 50 > screen_height:


rectangulo = pygame.Rect(10, 10, 50,50)

while True:
    screen.fill(back_color)

    pygame.draw.rect(screen, white _color, rectangulo)

    for even in pygame.even.get():
        if even.type == pygame.KEYDOWN:
    pygame.display.flip()
    clock.tick(60)

