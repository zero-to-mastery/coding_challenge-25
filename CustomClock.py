import turtle
import time

# Screen setup
window = turtle.Screen()
bgChoice = int(input("What color do you want the background to be? \n(pick a number.. 1- white, 2- black, 3- red, 4- blue): "))
bgChoice -= 1
bgList = ["white","black","red","blue"]
window.bgcolor(bgList[bgChoice])
window.setup(width=500, height=500)
window.title("Custom Clock Made By @Kooki-eByte")
window.tracer(0)

# Creating the pen
tu = turtle.Turtle()
tu.hideturtle()
tu.speed(0)
tu.pensize(4)


def createClock(h, m, s, tu):
	# The face of the clock
	tu.penup()
	tu.goto(0, 150)
	tu.setheading(180)
	tu.color("black")
	tu.pendown()
	tu.circle(150)

	# make the hours 1, 2, 3, 4...
	tu.penup()
	tu.goto(0,0)
	tu.setheading(90)

	for hours in range(12):
		tu.fd(130)
		tu.pendown()
		tu.fd(20)
		tu.penup()
		tu.goto(0,0)
		tu.rt(30)

	# make the seconds hand
	tu.penup()
	tu.goto(0,0)
	tu.setheading(90)
	tu.color("blue")
	rotation = (s / 60) * 360
	tu.rt(rotation)
	tu.pendown()
	tu.fd(75)

	# make the minute hand
	tu.penup()
	tu.goto(0,0)
	tu.setheading(90)
	tu.color("green")
	rotation = (m / 60) * 360
	tu.rt(rotation)
	tu.pendown()
	tu.fd(120)

	# make the hour hand
	tu.penup()
	tu.goto(0,0)
	tu.setheading(90)
	tu.color("red")
	rotation = (h / 12) * 360
	tu.rt(rotation)
	tu.pendown()
	tu.fd(60)

while True:
	hour = time.strftime("%I")
	minute = time.strftime("%M")
	second = time.strftime("%S")

	createClock(int(hour), int(minute), int(second), tu)

	window.update()
	time.sleep(1)
	tu.clear()



window.mainloop() # >>> Allows for the window to stay on after it finishes its initial boot up.