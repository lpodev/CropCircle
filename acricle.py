import turtle
import math

# Créer une fenêtre pour dessiner
window = turtle.Screen()
turtle.Screen().bgcolor('black')

# Créer une tortue pour dessiner
t = turtle.Turtle()

# Définir la taille et la vitesse de la tortue
t.shapesize(2)
t.speed(10)

# Définir la couleur de remplissage et de ligne
t.fillcolor('white')
t.pencolor('black')



# Dessiner les cercles internes
for i in range(4):
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.circle(50 + i * 10)

# Cacher la tortue
t.hideturtle()

# Attendre que l'utilisateur ferme la fenêtre
turtle.done()
