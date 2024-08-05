from game_of_life import Matrice
from random import random
from time import sleep

#   Example 1
P = {(0,4),(1,4),(0,5),(10,4),(10,5),(10,6),(11,3),(11,7),(12,2),(12,8),(13,2),(13,8),(14,5),(15,3),(15,7),(16,4),(16,5),(16,6),(17,5),(20,2),(20,3),(20,4),(21,2),(21,3),(21,4),(22,1),(22,5),(24,0),(24,1),(24,5),(24,6),(34,2),(34,3),(35,2),(35,3)}

population = Matrice(P, length=80, width=56)
#population.run(generation=None, position=(0,0), color="green", taille_cell=3, decal=1, color_back="0.75", time=0.1)

#   Example 2
P = {(2,8),(2,9),(3,8),(3,9),(5,6),(5,7),(5,8),(5,9),(6,2),(6,3),(6,5),(6,10),(7,2),(7,3),(7,5),(7,10),(8,5),(8,10),(8,12),(8,13),(9,5),(9,10),(9,12),(9,13),(10,6),(10,7),(10,8),(10,9),(12,6),(12,7),(13,6),(13,7),(6,8),(7,7),(8,7)}

population = Matrice(P, length=15, width=15)
#population.run(generation=None, position=(110,55), color="red", taille_cell=5, decal=1, color_back="0.75", time=0.1)

#   Example 3

P = {(3,3),(3,4),(3,5),(3,6),(3,7),(3,8),(4,3),(4,4),(4,5),(4,6),(4,7),(4,8),(3,10),(4,10),(5,10),(6,10),(7,10),(8,10),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(10,11),(10,10),(10,9),(10,8),(10,7),(10,6),(11,11),(11,10),(11,9),(11,8),(11,7),(11,6),(6,3),(7,3),(8,3),(9,3),(10,3),(11,3),(6,4),(7,4),(8,4),(9,4),(10,4),(11,4)}

population = Matrice(P, length=15, width=15)
population.run(generation=None, position=(110,55), color="red", taille_cell=5, decal=1, color_back="0.75", time=0.1)

#   Example 4
d = 90
P = {(d+x, d+y) for x in range(320-2*d) for y in range(222-2*d) if random() >= 0.3}

population = Matrice(P, length=320, width=222)

population.show(position=(0,0), color="black", taille_cell=1, decal=0)
sleep(2)

#population.run(generation=None, position=(0,0), color="black", taille_cell=1, decal=0, color_back="1", time=0.01)
