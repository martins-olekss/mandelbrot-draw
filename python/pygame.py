import pygame
import math
from pygame import gfxdraw

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

zoom = 150
iters = 100
w = 600
h = 600
size = [w, h]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

def cpl(a, b):
    return [a, b]

def cadd(p,q):
    c = cpl(
        p[0]+q[0],
        p[1]+q[1]
    )
    return c

def cmul(p,q):
    return cpl(
            p[0] * q[0] - p[1] * q[1],
            p[0] * q[1] + p[1] * q[0]
            )

def cmod(p):
    return math.sqrt(p[0] * p[0] + p[1] * p[1])

def is_in_mandelbrot_set(c, iterations):
    z = cpl(0, 0)
    while max(0, iterations):
        if (cmod(z) >= 2):
            return False
        z = cadd(cmul(z, z), c)
        iterations -= 1
    return True

def mandelbrot(w,h,zoom,iters):
    for x in range(w):
        for y in range(h):
            # scale our integer points
            # to be small real numbers around 0
            px = (x - w / 2) / zoom
            py = (y - h / 2) / zoom
            c = cpl(px, py)
            if (is_in_mandelbrot_set(c, iters)):
                gfxdraw.pixel(screen, x, y, RED)
        pygame.display.flip()

while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    screen.fill(WHITE)
    mandelbrot(w,h,zoom,iters)
    pygame.display.flip()
    pygame.image.save(screen, "screenshot.jpg")
    pygame.time.wait(50000)
pygame.quit()
