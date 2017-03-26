from pydojo import *

#create game display
screen(1280, 720)

pyco = Actor('example_library/pyco1.png', 'idle')
pyco.scale(0.2)
pyco.goto(100, 600)
pyco.speed = 5
# pyco.rotate = False
pyco.rotation = 'flip'

platforms = []

for i in range(6):
    a = Actor('example_library/platform.png', str(i))
    a.tag = 'flying platform'
    platforms.append(a)

terrain = Actor('example_library/terrain.png')
terrain.goto(CENTER.x, 700)
terrain.scale(1280, 50)

print(platforms)

for p in platforms:
    p.gorand()

pyco.jumping = False
pyco.onfloor = False

while True:

    if pyco.collide(terrain):
        pyco.onfloor = True
    elif not pyco.onfloor:
        for p in platforms:
            if pyco.collide(p):
                pyco.onfloor = True
    else:
        pyco.onfloor = False

    if key(RIGHT):
        pyco.point(90)
        pyco.forward(pyco.speed)
    if key(LEFT):
        pyco.point(-90)
        pyco.forward(pyco.speed)
    if keydown(UP):
        if pyco.onfloor:
            pyco.jumping = True
            t = 0

    if pyco.jumping:
        if t < 20:
            pyco.y -= 20
            t = t + 1

    if key(DOWN):
        pyco.point(180)
        pyco.forward(pyco.speed)
    if not pyco.onfloor:
        # print('falling')
        pyco.y += 10

    # for p in platforms:
    #     p.forward(1)

    update()