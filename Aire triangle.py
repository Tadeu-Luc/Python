from turtle import *            #Importation du module Turtle
print("AIRE D\'UN TRIANGLE")
b=0
h=0

while b<=0 and h<=0:
    b = int(input('entrer longueur en mètre : '))
    h = int(input('entrer hauteur en mètre : '))
    while b<=0 and h<=0:
        b = int(input('vous avez entrez une valeur erronée, entrer de nouveau la longueur en mètre : '))
        h = int(input('vous avez entrez une valeur erronée, entrer de nouveau la hauteur en mètre : '))
rt=b*h/2
print (rt)
print=("touche entrée pour continuer")
input ()
#déclaration variable x est initialement égal à 0

for x in range(3):      #Boucle tant que le compteur x n'atteint pas 5
    forward(rt)       #Avance la Turtle selon "cote"
    left(120)           #Pivote la Turtle de 144° vers la gauche
