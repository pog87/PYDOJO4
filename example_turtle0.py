from pydojo import *

screen(1280, 720)
fill(WHITE)

uga = Actor()
uga.pendown()

dimensione = 1
passi = 1

while True:
    uga.pensize = dimensione
    uga.forward(passi)
    uga.right(10)

    dimensione = dimensione + 1
    passi = passi + 1

    if keydown(ESCAPE):
        quit()

    update()