# module imports
import random
import numpy as np

# universal colors
bg = (255, 255, 255)  # background color 'white'
ln = (0, 0, 0)        # line color 'black'
tg = (255, 0, 127)    # tongue color 'red' variant

# Random face color applying to all table values. Starting with 50 range value produces brighter colors
rf = random.randint(50, 255)
gf = random.randint(50, 255)
bf = random.randint(50, 255)
face_random = [rf, gf, bf]
ce = face_random

# Random body color based on RGB value range
rb = random.randint(0, 255)
gb = random.randint(0, 255)
bb = random.randint(0, 255)
body_random = [rb, gb, bb]
dy = body_random

# Define random eye colors if rolled
re1 = random.randint(100, 255)
ge1 = random.randint(100, 255)
be1 = random.randint(100, 255)
eye1_random = [re1, ge1, be1]

re2 = random.randint(50, 255)
ge2 = random.randint(50, 255)
be2 = random.randint(50, 255)
eye2_random = [re2, ge2, be2]

re3 = random.randint(0, 255)
ge3 = random.randint(0, 255)
be3 = random.randint(0, 255)
eye3_random = [re3, ge3, be3]

# define random Snake Skin colors if rolled
rss = random.randint(0, 255)
gss = random.randint(0, 255)
bss = random.randint(0, 255)
snakeskin_random = [rss, gss, bss]

# chance for Hypnotize roll
for h in range(100):
        h = random.randint(0, 100)

        # Random number greater or equal to 95 generates Hypnotize
        if h >= 95:
                ey1 = eye1_random
                ey2 = eye2_random
                ey3 = eye3_random

        else:  # If unlucky, Reassign randomized eyes to RGB White
                ey1 = (255, 255, 255)
                ey2 = (255, 255, 255)
                ey3 = (255, 255, 255)

# chance for Snake Skin roll
for s in range(100):
        s = random.randint(0, 100)

        # Random number greater or equal to 95 generates Snake Skin
        if s >= 95:
                bb = snakeskin_random
        else:   # if unlucky bb values stay random body values defined above
                bb = dy

# chance for Fang roll
for f in range(100):
        f = random.randint(0, 100)

        # random number greater or equal to 92 generates Fangs
        if f >= 92:
                fa = (255, 255, 255)  # Fangs RGB value 'White'
        else: # if unlucky fa values stay random body values defined above
                fa = dy


# value array tables where Pythons are drawn with pixel value tied to "x" input

# garter type array table values
array_1 = np.array([
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 1
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 2
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 3
        [bg, bg, bg, bg, bg, bg, bg, ln, ln, ln, ln, bg, bg, ln, ln, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 4
        [bg, bg, bg, bg, bg, bg, ln, ce, ey1, ey2, ey1, ln, ln, ey3, ey2, ey3, ln, bg, bg, bg, bg, bg, bg, bg], # 5
        [bg, bg, bg, bg, bg, ln, ce, ce, ey2, ey3, ln, ce, ce, ey2, ey1, ln, ce, ln, bg, bg, bg, bg, bg, bg], # 6
        [bg, bg, bg, bg, bg, ln, dy, ce, ey3, ey2, ln, ce, ce, ey1, ey3, ln, ce, ce, ln, bg, bg, bg, bg, bg], # 7
        [bg, bg, bg, bg, bg, ln, dy, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg, bg], # 8
        [bg, bg, bg, bg, bg, ln, dy, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, dy, ln, bg, bg, bg, bg, bg], # 9
        [bg, bg, bg, bg, bg, ln, dy, dy, ce, ce, ce, ce, ce, ce, ce, ce, ce, dy, ln, bg, bg, bg, bg, bg], # 10
        [bg, bg, bg, bg, bg, bg, ln, ln, dy, ce, ce, ce, ce, ce, ce, dy, ln, ln, bg, bg, bg, bg, bg, bg], # 11
        [bg, bg, bg, bg, bg, bg, bg, ln, dy, ce, ce, ce, ce, ce, ce, dy, ln, bg, bg, bg, bg, bg, bg, bg], # 12
        [bg, bg, bg, bg, bg, bg, bg, ln, dy, dy, ce, ln, dy, ln, ce, dy, ln, bg, bg, bg, bg, bg, bg, bg], # 13
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, dy, dy, dy, dy, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 14
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ln, ln, ln, tg, ln, ln, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 15
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, fa, dy, tg, fa, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 16
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, dy, tg, tg, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 17
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, bb, tg, bb, bb, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 18
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, dy, dy, dy, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 19
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, bb, bb, bb, bb, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 20
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, dy, dy, dy, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 21
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, bb, bb, bb, bb, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 22
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, dy, dy, dy, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 23
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ce, bb, bb, bb, bb, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg]])  # 24

# rattler type array table values
array_2 =np.array([
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 1
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 2
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 3
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 4
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 5
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 6
        [bg, bg, bg, bg, bg, ln, ln, ln, ln, ln, ln, ln, ln, ln, ln, ln, ln, ln, bg, bg, bg, bg, bg, bg], # 7
        [bg, bg, bg, bg, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg, bg], # 8
        [bg, bg, bg, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg], # 9
        [bg, bg, bg, ln, ce, ce, bb, dy, bb, ln, ln, ln, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg], # 10
        [bg, bg, bg, ln, ce, bb, dy, bb, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg], # 11
        [bg, bg, bg, ln, ln, ln, ln, ln, ln, ln, ln, ln, ln, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg], # 12
        [bg, bg, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, ce, ce, ln, ln, ln, bg, bg, bg, bg, bg], # 13
        [bg, bg, ln, bb, ce, ey1, ey2, ce, ce, ce, ey3, ey1, ce, ln, ln, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 14
        [bg, bg, ln, dy, ce, ey3, ln, ce, ce, ce, ey2, ln, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 15
        [bg, bg, ln, bb, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 16
        [bg, bg, bg, ln, bb, dy, ce, ce, ce, bb, ce, ce, bb, ln, bg, bg, bg, bg, ln, bg, bg, bg, bg, bg], # 17
        [bg, bg, bg, ln, ln, bb, dy, bb, ln, dy, ln, bb, ln, bg, bg, bg, bg, ln, bb, ln, bg, bg, bg, bg], # 18
        [bg, bg, bg, ln, ce, ln, ln, ln, ln, ln, ln, ln, bg, bg, bg, bg, bg, ln, dy, ln, bg, bg, bg, bg], # 19
        [bg, bg, bg, ln, ce, bb, fa, bb, bb, fa, ln, bg, bg, bg, bg, bg, bg, ln, tg, ln, bg, bg, bg, bg], # 20
        [bg, bg, bg, ln, ce, fa, dy, bb, fa, bb, ln, bg, bg, bg, bg, bg, bg, ln, dy, ln, bg, bg, bg, bg], # 21
        [bg, bg, bg, ln, ce, dy, bb, bb, dy, dy, bb, ln, bg, bg, bg, bg, ln, dy, bb, ln, bg, bg, bg, bg], # 22
        [bg, bg, bg, ln, ce, bb, dy, dy, bb, dy, dy, ln, bg, bg, bg, bg, ln, tg, tg, ln, bg, bg, bg, bg], # 23
        [bg, bg, bg, ln, ce, dy, bb, dy, dy, bb, bb, ln, bg, bg, bg, ln, bb, dy, ln, bg, bg, bg, bg, bg]]) # 24

# cobra type array table values
array_3 = np.array([
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 1
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 2
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 3
        [bg, bg, bg, bg, bg, bg, bg, bg, ln, ln, ln, ln, ln, ln, ln, ln, ln, bg, bg, bg, bg, bg, bg, bg], # 4
        [bg, bg, bg, bg, bg, bg, bg, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg, bg, bg], # 5
        [bg, bg, bg, bg, bg, bg, bg, ln, ce, ey1, ln, ce, ce, ey2, ln, ce, ce, ce, ln, bg, bg, bg, bg, bg], # 6
        [bg, bg, bg, bg, bg, bg, ln, ln, ce, ey3, ln, ce, ce, ey1, ln, ce, ce, ce, ce, ln, bg, bg, bg, bg], # 7
        [bg, bg, bg, bg, bg, ln, ce, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, ce, ce, ln, bg, bg, bg], # 8
        [bg, bg, bg, bg, ln, ce, bb, ln, ce, ce, ce, ce, ce, ce, ce, ce, ce, ln, bb, ce, ln, bg, bg, bg], # 9
        [bg, bg, bg, bg, ln, ce, dy, ln, ce, ce, ln, ce, ln, ce, ce, ce, ln, dy, dy, ce, ln, bg, bg, bg], # 10
        [bg, bg, bg, bg, ln, ce, dy, ln, ln, ce, ce, ce, ce, ce, ce, ln, dy, dy, dy, ce, ln, bg, bg, bg], # 11
        [bg, bg, bg, bg, ln, ce, bb, bb, ln, ln, ln, tg, ln, ln, ln, bb, bb, bb, bb, ce, ln, bg, bg, bg], # 12
        [bg, bg, bg, bg, ln, ce, dy, dy, dy, fa, dy, tg, dy, dy, fa, dy, dy, dy, dy, ce, ln, bg, bg, bg], # 13
        [bg, bg, bg, bg, ln, ce, dy, dy, dy, fa, dy, tg, dy, dy, fa, dy, dy, dy, dy, ce, ln, bg, bg, bg], # 14
        [bg, bg, bg, bg, ln, ce, bb, bb, bb, bb, tg, tg, tg, bb, bb, bb, bb, bb, bb, ce, ln, bg, bg, bg], # 15
        [bg, bg, bg, bg, bg, ln, ce, dy, dy, dy, tg, dy, tg, dy, dy, dy, dy, dy, ce, ce, ln, bg, bg, bg], # 16
        [bg, bg, bg, bg, bg, ln, ce, dy, dy, dy, dy, dy, dy, dy, dy, dy, dy, dy, ce, ln, ln, bg, bg, bg], # 17
        [bg, bg, bg, bg, bg, bg, ln, ce, bb, bb, bb, bb, bb, bb, bb, bb, dy, ce, ce, ln, bg, bg, bg, bg], # 18
        [bg, bg, bg, bg, bg, bg, bg, ln, dy, dy, dy, dy, dy, dy, dy, dy, ce, ce, ln, bg, bg, bg, bg, bg], # 19
        [bg, bg, bg, bg, bg, bg, bg, ln, dy, dy, dy, dy, dy, dy, dy, ce, ce, ln, bg, bg, bg, bg, bg, bg], # 20
        [bg, bg, bg, bg, bg, bg, bg, ln, bb, bb, bb, bb, bb, dy, ce, ln, ln, bg, bg, bg, bg, bg, bg, bg], # 21
        [bg, bg, bg, bg, bg, bg, bg, ln, dy, dy, dy, dy, dy, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 22
        [bg, bg, bg, bg, bg, bg, bg, ln, dy, dy, dy, dy, dy, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 23
        [bg, bg, bg, bg, bg, bg, bg, ln, bb, bb, bb, bb, dy, dy, ce, ln, bg, bg, bg, bg, bg, bg, bg, bg]])  # 24

# mamba type array table values
array_4 = np.array([
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 1
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 2
        [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ln, ln, ln, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 3
        [bg, bg, bg, bg, bg, bg, ln, ln, ln, ln, ln, ln, ce, ln, ce, ce, ln, bg, bg, bg, bg, bg, bg, bg], # 4
        [bg, bg, bg, bg, bg, ln, ce, ce, ey1, ln, ey3, ce, ce, ce, ce, ce, ce, ln, bg, bg, bg, bg, bg, bg], # 5
        [bg, bg, bg, bg, bg, ln, ce, ce, ce, ce, ce, ce, ce, fa, dy, dy, fa, ln, bg, bg, bg, bg, bg, bg], # 6
        [bg, bg, bg, bg, ln, ce, ce, ce, ce, ce, ce, dy, dy, fa, dy, dy, fa, ln, bg, bg, bg, bg, bg, bg], # 7
        [bg, bg, bg, bg, ln, ce, ce, ce, ce, ce, dy, dy, fa, dy, dy, fa, ln, bg, bg, bg, bg, bg, bg, bg], # 8
        [bg, bg, bg, bg, ln, ce, ce, ce, ln, dy, dy, dy, dy, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 9
        [bg, bg, bg, bg, ln, ce, ce, ce, ln, dy, dy, dy, dy, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 10
        [bg, bg, bg, bg, ln, ce, ce, ce, ce, ln, dy, ln, ln, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 11
        [bg, bg, bg, bg, ln, ce, ce, ce, ce, ln, dy, dy, ln, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 12
        [bg, bg, bg, bg, ln, ce, ce, ce, ce, dy, ln, dy, dy, ln, ln, dy, ln, bg, bg, bg, bg, bg, bg, bg], # 13
        [bg, bg, bg, bg, ln, ce, ce, ce, dy, dy, ln, ln, dy, ln, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg], # 14
        [bg, bg, bg, bg, ln, ce, ce, ce, bb, bb, ln, bg, ln, ln, ln, ln, bg, bg, bg, bg, bg, bg, bg, bg], # 15
        [bg, bg, bg, bg, ln, ce, ce, ce, bb, bb, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 16
        [bg, bg, bg, bg, ln, ce, ce, ce, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 17
        [bg, bg, bg, bg, ln, ce, ce, ce, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 18
        [bg, bg, bg, bg, ln, ce, ce, ce, bb, bb, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 19
        [bg, bg, bg, bg, ln, ce, ce, ce, bb, bb, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 20
        [bg, bg, bg, bg, ln, ce, ce, ce, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 21
        [bg, bg, bg, bg, ln, ce, ce, ce, dy, dy, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 22
        [bg, bg, bg, bg, ln, ce, ce, ce, bb, bb, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg], # 23
        [bg, bg, bg, bg, ln, ce, ce, ce, bb, bb, ln, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]]) # 24

# this file is pulled into the main file where the body type is rolled and image is generated