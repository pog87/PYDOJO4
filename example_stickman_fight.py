from pydojo import *
# CREATE GAME DISPLAY
screen(1280, 720)

hero = Actor('example_asset/characters/stickman/kamae_idle')
hero.loadfolder('example_asset/characters/stickman/kisami_tsuki')
hero.loadfolder('example_asset/characters/stickman/mae_geri')
hero.loadfolder('example_asset/characters/stickman/yoko_geri')
hero.loadfolder('example_asset/characters/stickman/age_uke')
hero.loadfolder('example_asset/characters/stickman/gedan_barai')
hero.loadfolder('example_asset/characters/stickman/hit_body')
hero.action = 'kamae idle'
hero.rotation = 'flip'
hero.speed = 0
hero.x = 100

# MAIN LOOP
while True:

    hero.forward(hero.speed)

    # Movement Control
    if key(D):
        hero.point(90)
    if key(A):
        hero.point(-90)

    # Action Control
    if keydown(J):
        hero.action = 'kisami tsuki'
        print hero.action + '!'
    if keydown(K):
        hero.action = 'mae geri'
        print hero.action + '!'
    if keydown(L):
        hero.action = 'yoko geri'
        print hero.action + '!'
    if keydown(U):
        hero.action = 'age uke'
        print hero.action + '!'
    if keydown(I):
        hero.action = 'gedan barai'
        print hero.action + '!'
    if keydown(O):
        hero.action = 'gedan barai'
        print hero.action + '!'

    if hero.action == 'kamae idle':
        hero.speed = 0
        hero.slidecostumes(0, 23, pause=2)
    elif hero.action == 'kisami tsuki':
        hero.speed = 5
        hero.slidecostumes(24, 47, pause=0.5)
        if hero.cosnumber > 46:
            hero.action = 'kamae idle'
    elif hero.action == 'mae geri':
        hero.speed = 7
        hero.slidecostumes(48, 71, pause=1)
        if hero.cosnumber > 70:
            hero.action = 'kamae idle'
    elif hero.action == 'yoko geri':
        hero.speed = 5
        hero.slidecostumes(72, 95, pause=1)
        if hero.cosnumber > 94:
            hero.action = 'kamae idle'
    elif hero.action == 'age uke':
        hero.speed = -3
        hero.slidecostumes(96, 119, pause=0.5)
        if hero.cosnumber > 118:
            hero.action = 'kamae idle'
    elif hero.action == 'gedan barai':
        hero.speed = -5
        hero.slidecostumes(120, 143, pause=0.5)
        if hero.cosnumber > 142:
            hero.action = 'kamae idle'
    elif hero.action == 'hit body':
        hero.speed = -1
        hero.slidecostumes(144, 167, pause=1)
        if hero.cosnumber > 166:
            hero.action = 'kamae idle'

    # UPDATE SCREEN
    update()