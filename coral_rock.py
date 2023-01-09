from color import GRAY

import stddraw
import random
import sys


n = int(sys.argv[1])

x, y = 0, 0

for i in range(n):
    c = random.uniform(0, 1)
    cx, cy = x, y

    if 0.0 <= c < 0.4:
        x = 0.31 * cx - 0.53 * cy + 0.89
        y = -0.46 * cx - 0.29 * cy + 1.04

    if 0.4 <= c < 0.55:
        x = 0.31 * cx - 0.08 * cy + 0.22
        y = 0.15 * cx - 0.45 * cy + 0.34

    if 0.55 <= c <= 1.0:
        x = 0.55 * cy + 0.01
        y = 0.69 * cx - 0.20 * cy + 0.38

    stddraw.setPenRadius(0.0015)
    stddraw.setPenColor(GRAY)
    stddraw.point(x, y)
    stddraw.show(0)

stddraw.show()
