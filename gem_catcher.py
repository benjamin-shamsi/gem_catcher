import random

move = True

WIDTH = 800
HEIGHT = 600

spaceship = Actor('playership1_blue', (400, 560))
gem = Actor('gemgreen', (400, 0))

spaceship.score = 0

BG_Colour = (80, 0, 70)
GO_Colour = (80, 0, 70)

def draw():
    screen.fill(BG_Colour)

    GO_TxT = 'GAME OVER'
    screen.draw.text(GO_TxT, center = (400, 300), fontsize = 100, color = GO_Colour)

    gem.draw()
    spaceship.draw()

    screen.draw.text('SCORE: ' + str(spaceship.score), center = (60, 570), fontsize = 30, color = (250, 250, 250))


def update():
    global GO_Colour, move

    spaceship_mover()

    gem.y += 4 + spaceship.score / 5

    if gem.y > HEIGHT:
        GO_Colour = (0, 0, 0)

        gem_position()

    if gem.colliderect(spaceship):
        gem_position()
        spaceship.score += 1

    if gem.y > 600:
        GO_Colour = (0, 0, 0)

    if GO_Colour == (0, 0, 0):
        move = False


def gem_position():
    gem.y = 0
    gem.x = random.randint(20, 780)


def spaceship_mover():
    if keyboard.right:
        if spaceship.x <= 800:
            spaceship.x += 5
    if keyboard.left:
        if spaceship.x >= 0:
            spaceship.x -= 5


def on_mouse_move(pos):
    spaceship.x = pos[0]