from turtle import *
import math

"""
# Exercice 1: 
a=0
while a<12:
    a=a+1
    forward(150)
    left(150)

"""

"""
# Exercice 2:

# Question 1:

def triangle1(a):
    for _ in range(3):
        forward(a)  
        left(120)    
  
triangle1(200)
exitonclick()

# Question 2:

def triangle2(a):
    for _ in range(3):
        forward(a)  
        left(-120)    
  
triangle2(200)
exitonclick()

# Question 3:

def triangle3(a, angle):
    setheading(angle)
    for _ in range(3):
        forward(a)
        left(120)

triangle3(200, 10)
exitonclick()
"""

"""
# Exercice 3:

# Question 1:


def carre(a):
    color('red')
    for _ in range(4):
        forward(a)
        left(90)

# carre(100) 



# Question 2:

def ligneDeCarres(a, n):    
    for _ in range(n):
        carre(a) 
        up()
        forward(a * 2)
        down()

#ligneDeCarres(30, 5) 

#exitonclick()



def carresCroissants(a, n):
    taille_carré = a
    espace_entre_carrés = a / 4

    for _ in range(n):
        carre(taille_carré)  
        espace_entre_carrés *= 1.25 
        up()
        forward(taille_carré + espace_entre_carrés)
        down()
        taille_carré *= 1.25  
        
up()
setx(-300)
sety(0)
down()
carresCroissants(50, 5) 
exitonclick()
"""

"""
# Exercice 4:

speed(0) 
pensize(3) 
pencolor("purple")
fillcolor("orange") 

def dessiner_triangle(cote):
    begin_fill()
    for _ in range(3):
        forward(cote)
        right(120)
    end_fill()

def dessiner_carre(cote):
    begin_fill()
    for _ in range(4):
        forward(cote)
        right(90)
    end_fill()

def figuresPleines(n, cote):
    for i in range(n*2):
        if i % 2 == 0:
            dessiner_triangle(cote)
        else:
            dessiner_carre(cote)
        forward(cote)

    exitonclick()


figuresPleines(4, 20)

"""
"""

# Exercice 5: 

# Question 1:




def tracer_rayon(longueur):

    forward(longueur)
    backward(longueur)

def rayons(n, d):

    angle = 360 / n

    for _ in range(n):
        tracer_rayon(d) 
        left(angle) 

    exitonclick()

# rayons(18, 60)



# Question 2:

def polygone(a, n):
    angle = 360 / n

    for _ in range(n):
        forward(a) 
        left(angle)

    exitonclick()

# polygone(100, 6)




# Question 3:

def etoile(a, n):
    angle_sommet = 360 / n

    angle_saillie = 360 / (n * 2)

    for _ in range(n):
        forward(a) 
        right(angle_sommet)
        forward(a)
        left(180 - angle_saillie)  

    # exitonclick()

# etoile(100, 5)

def suiteEtoilesHorizontales(nb_etoiles, taille):
    nouveau_taille = taille
    for i in range(1, nb_etoiles + 1):
        etoile(nouveau_taille, 5) 
        espace_entre_etoiles = nouveau_taille * 2  
        up()
        forward(nouveau_taille + espace_entre_etoiles)
        down()

        if nb_etoiles % 2 == 0:
            if i == nb_etoiles/2 - 1:
                nouveau_taille = taille * 2
            elif i == nb_etoiles/2:
                nouveau_taille = taille * 2
            else:
                nouveau_taille = taille
        else:
                if i == (nb_etoiles - 1) / 2:
                    nouveau_taille = taille * 2
                else:
                    nouveau_taille = taille 


speed(0) 
up()
setx(-300)
sety(0)
down()
suiteEtoilesHorizontales(6, 20)  
exitonclick()

"""
