#Turtle Art Python Test
#December 6, 2016

#Import Area---
import turtle
import random
#--------------

#Variables----------------
length = (30)
hexturn = (60)
move = (length*1.75)
turn = (90)
notimes = (2)
michael = turtle.Turtle()
#--------------------------

#Functions--------------------------------
def getRGB(michael):
	turtle.colormode(255)
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	michael.color(r,g,b)

def shape(michael):
	getRGB(michael)
	michael.begin_fill()
	for i in range(6):
		michael.forward(length)
		michael.right(hexturn)
	michael.end_fill()

def outline(michael):
	michael.color('#ffffff')
	for i in range(6):
		michael.forward(length)
		michael.right(hexturn)

def next(michael):
	michael.pu()
	michael.right(turn)
	michael.forward(move)
	michael.left(turn)
	michael.pd()

def nextrow(michael):
	michael.pu()
	michael.left(turn)
	michael.forward(move*3)
	michael.left(30)
	michael.forward(length)
	michael.left(hexturn)
	michael.forward(length*1.1)
	michael.right(180)
	michael.pd()

def startpoint(michael):
	michael.pu()
	michael.setx(-60)
	michael.sety(-60)
	michael.forward(136)
	michael.left(turn)
	michael.forward(80)
	michael.right(turn)
	michael.pd()

def square(michael):
	michael.pu()
	michael.setx(-300)
	michael.sety(-300)
	michael.pd()
	getRGB(michael)
	michael.begin_fill()
	for i in range(4):
		michael.forward(600)
		michael.right(turn)
	michael.end_fill()

def end(michael):
	michael.pu()
	michael.setx(-300)
	michael.sety(-300)
	michael.pd()
#--------------------------------------------

#rawcode---------------------------------
michael.shape("circle")
michael.left(turn)
square(michael)
startpoint(michael)
for i in range(4):
	for i in range(4):
		shape(michael)
		outline(michael)
		next(michael)
	nextrow(michael)
end(michael)
#-----------------------------------------

turtle.done()
