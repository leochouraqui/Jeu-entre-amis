# By Léo Chouraqui | Marie-Estelle Chouraki | Chirozaan Srikantharajah | Kélia Siao

# Setup Python ----------------------------------------------- #
import pygame
import sys
import os
import random

from game import Game


# Setup pygame/window ---------------------------------------- #
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,32) # position de la fenetre
pygame.init()
pygame.display.set_caption('Combat d\'insultes entre amis')
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),0,32)

mainClock = pygame.time.Clock()



# Creation ---------------------------------------------------------#
game = Game(SCREEN)

# Fonctions ------------------------------------------------------- #
def redraw():
    SCREEN.fill((22,22,22))

    game.do() # rendre le jeu fonctionnel x)


def buttons():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE:
                game.sentences[1]["current"].append("Blabla")
            if event.key == pygame.K_RETURN:
                game.state = "score"
                game.player_turn = None


def update():
    pygame.display.update()
    mainClock.tick(60) # executer le jeu à 60 images par secondes (60FPS)


# Boucle ------------------------------------------------------- #
while True:

    # Dessiner --------------------------------------------- #
    redraw()

    # Boutons ------------------------------------------------ #
    buttons()

    # Mise à jour ------------------------------------------------- #
    update()
