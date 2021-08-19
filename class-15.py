import turtle

usaFlag = turtle.Turtle()
window = turtle.Screen()
usaFlag.speed(10)

# Function to make red rectangles
def redRect():
    usaFlag.color("#DC143C")
    usaFlag.begin_fill()
    usaFlag.forward(350)
    usaFlag.left(90)
    usaFlag.forward(30)
    usaFlag.left(90)
    usaFlag.forward(700)
    usaFlag.left(90)
    usaFlag.forward(30)
    usaFlag.left(90)
    usaFlag.forward(350)
    usaFlag.end_fill()

# Function to draw the strips of flag
def makeRectStrip(x,y):
    usaFlag.penup()
    usaFlag.goto(x,y)
    usaFlag.pendown()
    redRect()

# Call function to draw 7 red strips
makeRectStrip(0,-200)
makeRectStrip(0,-140)
makeRectStrip(0,-80)
makeRectStrip(0,-20)
makeRectStrip(0,40)
makeRectStrip(0,100)
makeRectStrip(0,160)
    
# Create a blue rectangle at the top of flag
usaFlag.color("#191970")
usaFlag.begin_fill()
usaFlag.goto(0,-20)
usaFlag.goto(0,190)
usaFlag.left(180)
usaFlag.forward(350)
usaFlag.left(90)
usaFlag.forward(210)
usaFlag.left(90)
usaFlag.forward(350)
usaFlag.end_fill()

# Function to draw star figure on map blue box
def star(x,y):
    usaFlag.penup()
    usaFlag.goto(x,y)
    usaFlag.pendown()
    usaFlag.color("#FFFFFF")
    usaFlag.begin_fill()
    # to draw star
    for i in range(5):
        usaFlag.forward(20)
        usaFlag.left(144)
    usaFlag.end_fill()

# First line with four stars
star(-300,150)
star(-220,150)
star(-140,150)
star(-60,150)

# Second line with four stars
star(-300,110)
star(-220,110)
star(-140,110)
star(-60,110)

# Third line with four stars
star(-300,70)
star(-220,70)
star(-140,70)
star(-60,70)

# Fourth line with four stars
star(-300,30)
star(-220,30)
star(-140,30)
star(-60,30)

turtle.done()

# Camel casing
# myNameIsRutuja