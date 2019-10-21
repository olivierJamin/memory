# coding: utf-8

"""
Jeu du Memory
Script Python
Fichiers : prgrm principal.py, constantes.py, n1, n2 + images
"""
import sys, pygame
import random,time
from pygame.locals import *
from config import *
pygame.init()

fenetre = pygame.display.set_mode((largeurx_fenetre,hauteury_fenetre))

#importation des images communes
fond = pygame.image.load(backgroundFile).convert()
fond = pygame.transform.scale(fond,(dim_fond))

dos = pygame.image.load(dosFile).convert_alpha()
dos = pygame.transform.scale(dos,(dim_carte))

#importation des cartes et ajout dans le referentiel des cartes
liste_ref_carte = []
bonobo = pygame.image.load(bonoboFile).convert_alpha()
bonobo = pygame.transform.scale(bonobo,(dim_carte))
liste_ref_carte.append(bonobo)

gorille = pygame.image.load(gorilleFile).convert_alpha()
gorille = pygame.transform.scale(gorille,(dim_carte))
liste_ref_carte.append(gorille)

gibbon = pygame.image.load(gibbonFile).convert_alpha()
gibbon = pygame.transform.scale(gibbon,(dim_carte))
liste_ref_carte.append(gibbon)

orang_outang = pygame.image.load(orangOutangFile).convert_alpha()
orang_outang = pygame.transform.scale(orang_outang,(dim_carte))
liste_ref_carte.append(orang_outang)

tamarin_empereur = pygame.image.load(tamarinEmpereurFile).convert_alpha()
tamarin_empereur = pygame.transform.scale(tamarin_empereur,(dim_carte))
liste_ref_carte.append(tamarin_empereur)

nasique = pygame.image.load(nasiqueFile).convert_alpha()
nasique = pygame.transform.scale(nasique,(dim_carte))
liste_ref_carte.append(nasique)

# un couple de carte par carte
liste_carte = []
for carte in range(0,nbCarte):
    liste_carte.append(carte)
    liste_carte.append(carte)
# mélange de la liste
random.shuffle(liste_carte)
#liste dans tableau de jeu
tableau_jeu = []
for ligne in range (0,nbLigne) :
    listeTemp = []
    for colonne in range(0,nbColonne) :
        listeTemp.append(liste_carte[(ligne*nbColonne) + colonne])
    tableau_jeu.append(listeTemp)

print(liste_carte) #debug
print(tableau_jeu) #debug


# affichage initial du jeu : toutes les cartes sont retournée, dos visible
fenetre.blit(fond, (0,0))
for ligne in range (0,nbLigne):
    for colonne in range(0,nbColonne):
        fenetre.blit(dos,(marge+(colonne*(largeurx_carte + marge)),marge+ligne*(hauteury_carte + marge)))
pygame.display.flip()
tour = 1

#boucle principale de jeu
continuer = 1
while continuer:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer=0
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer=0
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            #recuperation de la ligne et de la colonne
            indiceColonne = event.pos[0]//(largeurx_carte + marge)
            indiceLigne = event.pos[1]//(hauteury_carte + marge)
            #suppression de la marge
            if ((event.pos[0] > (indiceColonne*(largeurx_carte + marge)+marge)) and (event.pos[1] > (indiceLigne*(hauteury_carte + marge)+marge))) :
                # on sauvergarde sa valeur
                indiceCarte = tableau_jeu[indiceLigne][indiceColonne]
                # on recherche sa reference
                carte = liste_ref_carte[indiceCarte]
                # on la retourne
                fenetre.blit(carte,(marge+indiceColonne*(largeurx_carte + marge),marge+indiceLigne*(hauteury_carte + marge)))
                if tour == 1 : 
                # si c'est la premiere carte, on sauvergarde le contexte
                    indiceColonne1 = indiceColonne
                    indiceLigne1 = indiceLigne
                    indiceCarte1 = indiceCarte
                    tour = 2
                else :
                # c'est la deuxieme carte
                    tour = 1
                    if (indiceCarte != indiceCarte1) :
                        # les cartes sont differentes
                        # on garde un peu l'affichage : 5 secondes
                        pygame.display.flip()
                        time.sleep(5)
                        # on remet les dos
                        fenetre.blit(dos,(marge + indiceColonne1*(largeurx_carte + marge),marge + indiceLigne1*(hauteury_carte + marge)))
                        fenetre.blit(dos,(marge + indiceColonne*(largeurx_carte + marge),marge + indiceLigne*(hauteury_carte + marge)))
                #on affiche
                pygame.display.flip()
