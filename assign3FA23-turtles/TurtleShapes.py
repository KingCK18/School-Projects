'''
TurtleShapes.py

@author: christiankirby
'''

import turtle, BoundingBox

def drawOneShape(t, size):
    """
    A function that draws a square with a side length of 50
    """

    for i in range(4):
        t.forward(50)
        t.left(90)
    t.pendown()
def drawOneStar(t,size):
    """
    A function that draws the shape of a star
    """
    t.penup()
    t.backward(100)
    t.pendown()
    for i in range(5):
        t.forward(60)
        t.right(144)
        t.forward(60)
        t.left(72)
    t.up()

if __name__ == '__main__':
    win = turtle.Screen()
    t = turtle.Turtle()
    BoundingBox.drawBoundingBox()
    drawOneShape(t,5)
    drawOneStar(t,10)
    
    win.exitonclick()
    