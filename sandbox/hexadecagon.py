#Hexadecagon
#November 26, 2016

#Imports----------
import turtle
import random
#-----------------

#Variables------------------
michael = turtle.Turtle()
forward = (50)
turn = (22.5)
#----------------------------

#Functions-------------------
def hexadegagon(michael):
	for i in range(16):
		michael.forward(forward)
		michael.right(turn)
#----------------------------

#Random RGB color value
turtle.colormode(255)
r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
michael.color(r,g,b)

hexadegagon(michael)

turtle.done()
