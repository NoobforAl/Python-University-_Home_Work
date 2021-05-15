import sys, random, stddraw
from color import DARK_GREEN, GRAY
n = int(sys.argv[1])
x,y = 0, 0
for i in range(n):
    cx = x
    cy = y
    c = random.uniform(0, 1)
    if c < 0.02:
        x = 0.50
        y = 0.27 * cy
    if 0.02 <= c < 0.17 :
        x = (-0.14 * cx) + (0.26 * cy) + 0.57
        y = (0.25 * cx) + (0.22 * cy) - 0.04
    if 0.17 <= c < 0.3:
        x = (0.17 * cx) - (0.21 * cy) + 0.41
        y = (0.22 * cx) + (0.18 * cy) + 0.09
    if 0.3 <= c <= 1.0:
        x = (0.78 * cx) + (0.03 * cy) + 0.11
        y = (-0.03 * cx) + (0.74 * cy) + 0.27
    stddraw.setPenRadius(0.00001)
    stddraw.setPenColor(DARK_GREEN)
    stddraw.point(x, y)
    stddraw.show(0)
stddraw.show()

