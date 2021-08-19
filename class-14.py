import turtle

indianFlag = turtle.Turtle()
window = turtle.Screen()
window.title("Indian Flag")
indianFlag.speed(6)
# count = 10
indianFlag.pensize(3)


# To draw center chakra
indianFlag.color("#000080")
indianFlag.begin_fill()
for i in range(24):
    indianFlag.forward(100)
    indianFlag.backward(100)
    # count = count + 1
    indianFlag.right(15)
indianFlag.end_fill()

indianFlag.goto(0,-100)

''' To draw a circle around the lines '''
# indianFlag.color("#800000")
# indianFlag.begin_fill()
indianFlag.circle(100, 360)
# indianFlag.end_fill()

indianFlag.penup()
indianFlag.goto(0,-150)
indianFlag.pendown()

indianFlag.color("green")
indianFlag.begin_fill()
indianFlag.forward(350)
indianFlag.right(90)
indianFlag.forward(100)
indianFlag.right(90)
indianFlag.forward(700)
indianFlag.right(90)
indianFlag.forward(100)
indianFlag.right(90)
indianFlag.forward(350)
indianFlag.end_fill()


indianFlag.penup()
indianFlag.goto(0,150)
indianFlag.pendown()

indianFlag.color("orange")
indianFlag.begin_fill()
indianFlag.forward(350)
indianFlag.left(90)
indianFlag.forward(100)
indianFlag.left(90)
indianFlag.forward(700)
indianFlag.left(90)
indianFlag.forward(100)
indianFlag.left(90)
indianFlag.forward(350)
indianFlag.end_fill()
# Paramter (radius, degree of ratation)
turtle.done()