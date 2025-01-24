import turtle as t
import os

player_a_score = 0
player_b_score = 0

windowdow=t.Screen()
windowdow.title("Jeux Pong")
windowdow.bgcolor("black") #couleur de fond
windowdow.setup(width=600,height=400)
windowdow.tracer(0) #définir la vitesse de l'écran

# création de la raquette gauche

paddle_left = t.Turtle()
paddle_left.shape('square')
paddle_left.color("white")
paddle_left.shapesize(stretch_wid=5,stretch_len=1) #forme de la raquette
paddle_left.penup()
paddle_left.goto(-350,0) #position de la raquette

# création de la raquette droite

paddle_right = t.Turtle()
paddle_right.shape('square')
paddle_right.color("white")
paddle_right.shapesize(stretch_wid=5,stretch_len=1) #forme de la raquette
paddle_right.penup()
paddle_right.goto(350,0) #position de la raquette

ball = t.Turtle()
ball.speed(0)
ball.shape('circle') #Forme de la balle
ball.color("white")
ball.goto(0,0)
ball_dx= 1.5 #la direction du mouvement de la balle en x
ball_dy= 1.5 #la direction du mouvement de la balle en y

#Tableau de bord

pen = t.Turtle()
pen.speed(0) #vitesse
pen.color('white')
pen.hideturtle()
pen.goto(0, 260) #position x, y
pen.write("Joueur 1: 0      Player B: 0",align="center",font=('Monaco',24,"normal")) #alignement
