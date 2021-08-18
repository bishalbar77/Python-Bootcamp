import turtle

indianFlag = turtle.Turtle()
window = turtle.Screen()
window.title("Indian Flag")
indianFlag.speed(6)
# count = 10
indianFlag.pensize(3)

for i in range(24):
    indianFlag.forward(100)
    indianFlag.backward(100)
    # count = count + 1
    indianFlag.left(15)
indianFlag.goto(0,-100)
indianFlag.circle(100, 360)

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

# Paramter (radius, degree of ratation)
turtle.done()