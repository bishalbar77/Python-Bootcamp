# import turtle

# turtle.
from turtle import *
# from <Package_name> import <what_functions_you_need>

marker = Turtle()
# Create a object from Turtle class 
# Screen operations
window = Screen()
# Create a object from Screen class 
window.title("My Turtle Project")
# To change window title

# This is how we make an object
marker.shape('turtle')
# To change the of marker
# Some shapes :- 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'

marker.turtlesize(1)
# To increase the size of marker by some percent
marker.speed(1)
marker.color("#EEEEEE")
# To change the speed if the marker
# 'fastest' :  0
# 'fast'    :  10
# 'normal'  :  6
# 'slow'    :  3
# 'slowest' :  1
marker.color("yellow")
marker.begin_fill()
marker.forward(100)
# To move the marker in forward direction
marker.left(90)
# To move the marker angle to left by 90
marker.forward(100)
marker.left(90)
marker.forward(100)
marker.left(90)
marker.forward(100)
marker.left(90)
marker.end_fill()


marker.color("#ADD8E6")
marker.begin_fill()
# Next bottom sqaure
marker.forward(100)
marker.right(90)
marker.forward(100)
marker.right(90)
marker.forward(100)
marker.right(90)
marker.forward(100)
marker.right(90)
marker.end_fill()


window.bgcolor("green")
# To change the background color
done() 