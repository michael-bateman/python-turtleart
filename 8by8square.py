#other class Turtle Art Test
#December 2, 2016

#imports--------
import turtle
import random
#---------------

#variables-------------------
forward = (25)
turn = (90)
blank = (30)
michael = turtle.Turtle()
#----------------------------

#functions-------------------------------
def randomcolor(michael):
	turtle.colormode(255)
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	michael.color(r,g,b)

def square(michael):
	randomcolor(michael)
	michael.begin_fill()
	for i in range(4):
		michael.forward(forward)
		michael.right(turn)
	michael.end_fill()

def nextsquare(michael):
	michael.pu()
	michael.forward(forward)
	michael.right(turn)
	michael.forward(forward + blank)
	michael.left(turn)
	michael.backward(forward)
	michael.pd()

def row(michael):
	michael.pu()
	michael.left(turn)
	michael.forward(forward * 8)
	michael.forward(blank * 8)
	michael.left(turn)
	michael.forward(forward + blank)
	michael.right(180)
	michael.pd()
#-------------------------------------------

#raw code------------------------
michael.speed(10)
michael.left(90)
for i in range(8):
	for i in range(8):
		randomcolor(michael)
		square(michael)
		nextsquare(michael)
	row(michael)
#----------------------------------

turtle.done()
