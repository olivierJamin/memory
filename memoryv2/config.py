
#Paramètres de la fenêtre
largeurx_fenetre = 600
hauteury_fenetre = 400

#Paramètres fond d'écran
dim_fond = (largeurx_fenetre),(hauteury_fenetre)

#Paramètres plateau de jeu
nbColonne = 4
nbLigne = 3
marge = 20

#Paramètres carte
nbCarte = 6
largeurx_carte = (largeurx_fenetre - (nbColonne+1)*marge)//nbColonne
hauteury_carte = (hauteury_fenetre - (nbLigne+1)*marge)//nbLigne
dim_carte = (largeurx_carte),(hauteury_carte)
#images
pathImage="ressources/"
pathCarte=pathImage + "cartes/"
#
backgroundFile = pathImage + "background.jpg"
dosFile = pathImage + "dos_carte.png"
#
bonoboFile = pathCarte + "bonobo.png"
gibbonFile = pathCarte + "gibbon.png"
gorilleFile = pathCarte + "gorille.png"
nasiqueFile = pathCarte + "nasique.png"
orangOutangFile = pathCarte + "orang_outan.png"
rasimFile = pathCarte + "rasim.jpg"
tamarinEmpereurFile = pathCarte + "tamarin_empereur.png"


