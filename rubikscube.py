import turtle
import random

michael = turtle.Turtle()
forward = (50)
turn = (90)

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

michael.left(turn)
for i in range(3):
	for i in range(3):
		square(michael)
		nextsquare(michael)
	nextrow(michael)

turtle.done()