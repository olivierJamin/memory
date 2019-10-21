# coding: utf-8

"""
Jeu du Memory
Script Python
Fichiers : prgrm principal.py, constantes.py, n1, n2 + images
"""
import sys, pygame
import random
from pygame.locals import *
from constantes import *
pygame.init()

#ouverture de la fenêtre de jeu
fenetre = pygame.display.set_mode((largeurx_fenetre,hauteury_fenetre))

#importation des images
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))
fond = pygame.transform.scale(fond,(dim_fond))

dos = pygame.image.load("dos_carte.png").convert_alpha()
dos = pygame.transform.scale(dos,(dim_carte))

bonobo = pygame.image.load("bonobo.png").convert_alpha()
bonobo = pygame.transform.scale(bonobo,(dim_carte))

rasim = pygame.image.load("rasim.jpg").convert_alpha()
rasim = pygame.transform.scale(rasim,(dim_carte))

gibbon = pygame.image.load("gibbon.png").convert_alpha()
gibbon = pygame.transform.scale(gibbon,(dim_carte))

orang_outan = pygame.image.load("orang_outan.png").convert_alpha()
orang_outan = pygame.transform.scale(orang_outan,(dim_carte))

tamarin_empereur = pygame.image.load("tamarin_empereur.png").convert_alpha()
tamarin_empereur = pygame.transform.scale(tamarin_empereur,(dim_carte))

nasique = pygame.image.load("nasique.png").convert_alpha()
nasique = pygame.transform.scale(nasique,(dim_carte))

#création des listes de cartes
liste_dos = [dos,dos,dos,dos,dos,dos,dos,dos,dos,dos,dos,dos]

liste_carte = [bonobo,bonobo,rasim,rasim,gibbon,gibbon,orang_outan,orang_outan,tamarin_empereur,tamarin_empereur,nasique,nasique]
random.shuffle(liste_carte) #cette fonction permet de mélanger la liste du dessus

#définition des coordonnées des cartes avec 2 listes
liste_coordonneesx = [50,50*2+l,50*3+2*l,50*4+3*l] #pour les abscisses
liste_coordonneesy = [50,50*2+h,50*3+2*h]#pour les ordonnées

#boucle principale de jeu
continuer = 1
while continuer:
    pygame.display.flip()
    for event in pygame.event.get():
        n=0
        for i in range(0,4):
            for j in range (0,3):
                fenetre.blit(liste_dos[n], (liste_coordonneesx[i],liste_coordonneesy[j]))
                n=n+1
        n=0
        for i in range(0,4):
            for j in range (0,3):
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and liste_coordonneesx[i] < event.pos[0] < (liste_coordonneesx[i]+l) and liste_coordonneesy[j] < event.pos[1] < (liste_coordonneesy[j]+h) :
                    fenetre.blit(liste_carte[n], (liste_coordonneesx[i],liste_coordonneesy[j]))
                    pygame.display.flip()
                    afficher=1
                    while afficher==1:
                        n1=liste_carte[n]
                        for event in pygame.event.get():
                            m=0
                            for i in range(0,4):
                                for j in range (0,3):
                                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and liste_coordonneesx[i] < event.pos[0] < (liste_coordonneesx[i]+l) and liste_coordonneesy[j] < event.pos[1] < (liste_coordonneesy[j]+h) :
                                        n2=liste_carte[m]
                                        fenetre.blit(liste_carte[m], (liste_coordonneesx[i],liste_coordonneesy[j]))
                                        pygame.display.flip()
                                        if n1==n2:
                                            afficher=0
                                            fenetre.blit(fond,(0,0))
                                        else:
                                            afficher=0
                            m=m+1
                n=n+1


        if event.type == QUIT:
            continuer=0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer=0




