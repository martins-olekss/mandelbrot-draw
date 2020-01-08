#!python
import math
import time
from datetime import datetime
from time import mktime
from PIL import Image

# Code ported using: https://stackoverflow.com/questions/3725522/fractals-explained
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
                print("x " + str(x) + ":y " + str(y))
                pixels[x, y] = (255, 255, 255, 255)

zoom = 1000
iters = 100
w = 5000
h = 5000
background = (0, 0, 0, 255)
image = Image.new("RGBA", (w, h), background)
pixels = image.load()

mandelbrot(w,h,zoom,iters)
t = datetime.now()
unix_secs = mktime(t.timetuple())
filename = str(int(unix_secs)) + "w" + str(w) + "h" + str(h) + "_mandelbrot.png";
image.save(filename)
