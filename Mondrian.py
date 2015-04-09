#  File: Mondrian.py

#  Description: Will make random, abstract mondrian influenced art.

#  Student Name: Garner Vincent

#  Date Created:3-2-15

#  Date Last Modified:3-7-15


import turtle
import random

def drawSquare(ttl, color, xlow, ylow, xhigh, yhigh):
	#this function fills in the squares with the fill color assigned previously
	ttl.color('black', color)
	ttl.penup()
	ttl.goto(xlow, ylow)
	ttl.begin_fill()
	ttl.pendown()
	ttl.goto(xlow, yhigh)
	ttl.goto(xhigh, yhigh)
	ttl.goto(xhigh, ylow)
	ttl.goto(xlow, ylow)
	ttl.end_fill()
	ttl.color('black')

def drawLine(ttl, x1, y1, x2, y2):
	#draws lines from one point to another
	ttl.penup()
	ttl.goto(x1, y1)
	ttl.pendown()
	ttl.goto(x2, y2)

def pickDirection(ttl, level):
	#function to randomly pick horizontal or vertical line
	if level < 2:
		pick = random.randint(1, 2)
		return pick
	else:
		randFlt = random.random()
		if level == 2:
			if randFlt <= .146:
				pick = 3
			else:
				pick = random.randint(1, 2)
		elif level == 3:
			if randFlt <= .192:
				pick = 3
			else:
				pick = random.randint(1, 2)
		elif level == 4:
			if randFlt <= .238:
				pick = 3
			else:
				pick = random.randint(1, 2)
		elif level == 5:
			if randFlt <= .284:
				pick = 3
			else:
				pick = random.randint(1, 2)
		elif level >= 6:
			if randFlt <= .33:
				pick = 3
			else:
				pick = random.randint(1, 2)
	return pick

def pickColor(ttl, level, pick, xlow, ylow, xhigh, yhigh):
	#function to randomly pick color before passing to the square fill functi
	color = random.randint(1, 5)
	if color == 1: 
		#salmon
		color = '#FF9999'
	elif color == 2:
		#mint
		color = 'white'
	elif color == 3:
		color = 'white'
	elif color == 4:
		#pale yellow
		color = '#FFFF99' 
	elif color == 5:
		#light blue
		color = '#3399FF'

	drawSquare(ttl, color, xlow, ylow, xhigh, yhigh)
		
def mondrian(ttl, level, xlow, xhigh, ylow, yhigh):
	#recursive mondrian functino which will go down levels in order to randomly split areas either vertically or horizontally
	if level == 0:
		return
	else:
		pick = pickDirection(ttl, level)

		#split the vertical and horizontal picks because a veritcal will generate an x-val while a horizontal will generate a y-val
		#vertical pick
		if pick == 1:
			if not ((xhigh - (50 // level)) - (xlow + 50 // level)) < 0:
				x = random.randint(xlow + 50 // level, xhigh - 50 // level)
			else:
				x = (xlow + xhigh) // 2
			drawLine(ttl, x, ylow, x, yhigh)

			if level == 1:
				pickColor(ttl, level, pick, x, ylow, xhigh, yhigh)

			mondrian(ttl, level - 1, x, xhigh, ylow, yhigh)
			mondrian(ttl, level - 1, xlow, x, ylow, yhigh)

		#horitzontal pick
		elif pick == 2:
			if not ((yhigh - 50 // level) - (ylow + 50 // level)) < 0:
				y = random.randint(ylow + 50 // level, yhigh - 50 // level)
			else:
				y = (ylow + yhigh) // 2
			drawLine(ttl, xlow, y, xhigh, y)

			if level == 1:
				pickColor(ttl, level, pick, xlow, y, xhigh, yhigh)

			mondrian(ttl, level - 1, xlow, xhigh, y, yhigh) 
			mondrian(ttl, level - 1, xlow, xhigh, ylow, y)

		#blank pick 
		elif pick == 3:
			mondrian(ttl, level - 1, xlow, xhigh, ylow, yhigh)
		

def main():
  #create turtle object
  ttl = turtle.Turtle()

  # put label on top of page
  turtle.title ('Mondrian Art')

  # setup screen size
  turtle.setup (900, 900, 0, 0)

  #have use enter level of recursion
  level = int(input('Enter a level of recursion between 1 and 6: '))

  ttl.speed(0)
  ttl.pensize(4)
  ttl.color('black')
  turtle.hideturtle()

  mondrian(ttl, level, -400, 400, -400, 400)

  ttl.penup()
  ttl.goto(-400, -400)
  ttl.pendown()
  ttl.goto(-400, 400)
  ttl.goto(400, 400)
  ttl.goto(400, -400)
  ttl.goto(-400, -400)
  ttl.penup()
  can = turtle.getscreen().getcanvas()
  can.postscript(file = './Mondrian.ps')


  turtle.done()
 


main()