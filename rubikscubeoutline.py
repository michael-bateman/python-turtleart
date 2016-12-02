#rubics cube with frame
#December 2, 2016

#imports----------
import turtle
import random
#-----------------

#variables---------------------
michael = turtle.Turtle()
forward = (50)
turn = (90)
#------------------------------

#functions-------------------------------
def square(michael):
	turtle.colormode(255)
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	michael.color(r,g,b)
	michael.begin_fill()
	for i in range(4):
		michael.forward(forward)
		michael.right(turn)
	michael.end_fill()

def nextsquare(michael):
	michael.pu()
	michael.forward(forward)
	michael.pd()

def nextrow(michael):
	michael.pu()
	michael.backward(forward * 3)
	michael.right(turn)
	michael.forward(forward)
	michael.left(turn)
	michael.pd()

def circle(michael):
	michael.pu()
	michael.right(turn)
	michael.forward(200)
	michael.left(turn)
	michael.pd()
	michael.color('#FFC0CB')
	michael.begin_fill()
	michael.circle(200,360)
	michael.end_fill()

def reset(michael):
	michael.pu()
	michael.setx(0)
	michael.sety(0)
	michael.backward(75)
	michael.left(turn)
	michael.backward(75)
	michael.pd()
#--------------------------------------

#raw code--------------------
michael.left(turn)
circle(michael)
reset(michael)
for i in range(3):
	for i in range(3):
		square(michael)
		nextsquare(michael)
	nextrow(michael)
#-----------------------------

turtle.done()