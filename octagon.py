#Sandbox code
#November 26, 2016

#Imports-------
import turtle
import random
#--------------

#Variables-----------------
forward = (50)
turn = (45)
michael = turtle.Turtle()
#---------------------------

#Functions-------------------------
def octagon(michael):
	for i in range(8):
		michael.forward(forward)
		michael.right(turn)
#----------------------------------

#Random RGB colour value
turtle.colormode(255)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
michael.color(r,g,b)

octagon(michael)

turtle.done()