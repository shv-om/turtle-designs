import turtle

cursor = turtle.Turtle()

turtle.bgcolor("black")
cursor.pensize(2)
colorlist = ['red', 'blue', 'pink', 'orange', 'purple', 'green']

def design0(num):
	for j in range(num):
		c = colorlist[j%6]
		cursor.color(c)
		cursor.forward(j*4)
		cursor.left(70+j)

def design1(num):
	for j in range(num):
		c = colorlist[j%6]
		cursor.color(c)
		cursor.forward(j*2)
		cursor.left(80)

def design2(num):
	for j in range(num):
		c = colorlist[j%6]
		cursor.color(c)
		cursor.forward(j)
		cursor.left(61)

def design3(num):
	for i in range(num):
		c = colorlist[i%4]
		cursor.color(c)
		cursor.circle((i*2), 50)
		cursor.left(45)


n = int(input("Enter a Number to start: "))

cursor.penup()
cursor.setpos(-200, 200)
cursor.pendown()
design1(n)

cursor.penup()
cursor.setpos(200, 200)
cursor.pendown()
design0(n)

cursor.penup()
cursor.setpos(-200, -200)
cursor.pendown()
design2(n)

cursor.penup()
cursor.setpos(200, -200)
cursor.pendown()
design3(n)

input("Enter to exit")

