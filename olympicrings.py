#Turtle Art Olympic Rings
#November 26, 2016

#Import Zone----
import turtle
#---------------

#Variables----------------
length = (50)
turn =(90)
michael = turtle.Turtle()
#--------------------------

#Function to make a circle
def circle(michael):
	michael.circle(length,360)

#Function to make turtle to move to the next ring
def move(michael):
	michael.pu()
	michael.right(turn)
	michael.forward(length * 2.25)
	michael.left(turn)
	michael.pd()

#Function to make turtle move to next row
def nextrow(michael):
	michael.pu()
	michael.left(turn)
	michael.forward(length * 1.125 * 2 + length)
	michael.left(turn)
	michael.forward(length * 1)
	michael.right(turn * 2)
	michael.pd()


michael.left(turn)

#Blue Ring
michael.color('#0000FF')
circle(michael)
move(michael)

#Black Ring
michael.color('#000000')
circle(michael)
move(michael)

#Red Ring
michael.color('#ff0000')
circle(michael)

#Yellow Ring
michael.color('#ffff00')
nextrow(michael)
circle(michael)
move(michael)

#Green Ring
michael.color('#008000')
circle(michael)

turtle.done()