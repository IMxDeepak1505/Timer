import time
import datetime as dt
import turtle


# create a turtle to display time
t = turtle.Turtle()

# create a turtle to create rectangle box
t2 = turtle.Turtle()

# create screen
s = turtle.Screen()

# set background color of the screen
s.bgcolor("yellow")

# obtain current hour, minute and second
# from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t2.pensize(3)
t2.color('black')
t2.penup()

# set the position of turtle
t2.goto(-5, 0)
t2.pendown()

# create rectangular box
for i in range(2):
	t2.forward(200)
	t2.left(90)
	t2.forward(70)
	t2.left(90)

# hide the turtle
t.hideturtle()

while True:
	t.hideturtle()
	t.clear()
	# display the time
	t.write(str(hr).zfill(2)
			+ ":"+str(min).zfill(2)+":"
			+ str(sec).zfill(2),
			font=("Arial Narrow", 35, "bold"))
	time.sleep(1)
	sec += 1

	if sec == 60:
		sec = 0
		min += 1

	if min == 60:
		min = 0
		hr += 1

	if hr == 13:
		hr = 1
