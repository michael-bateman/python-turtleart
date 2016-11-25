import turtle
import random

length = (25)
hexturn = (60)
move = (length*1.75)
turn = (90)
notimes = (2)

michael = turtle.Turtle()

def wholefunction(michael):
	michael.left(turn)
	for i in range(notimes):
		for i in range(4):
			turtle.colormode(255)
			r = random.randint(0,255)
			g = random.randint(0,255)
			b = random.randint(0,255)
			michael.color(r,g,b)
			michael.begin_fill()
			for i in range(6):
				michael.forward(length)
				michael.right(hexturn)
			michael.end_fill()
			turtle.colormode(255)
			r = random.randint(0,255)
			g = random.randint(0,255)
			b = random.randint(0,255)
			michael.color(r,g,b)
			for i in range(6):
				michael.forward(length)
				michael.right(hexturn)
			michael.pu()
			michael.right(turn)
			michael.forward(move)
			michael.left(turn)
			michael.pd()
		michael.pu()
		michael.left(turn)
		michael.forward(move*4)
		michael.left(30)
		michael.forward(length)
		michael.left(hexturn)
		michael.forward(length)
		michael.right(180)
		michael.pd()

wholefunction(michael)

turtle.done()