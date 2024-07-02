'''
DrawRow.py

@author: YOUR NAME HERE
'''

import turtle, BoundingBox, TurtleShapes

def drawRowsOfRows(t, func):
    """
    Draws ten rows of a shape with varying sizes
    """
    num_rows = 10
    num_shapes_per_row = 10

    for row in range(num_rows):
        y = 500 * row * 2
        size = 40 + row * 10
        for i in range(num_shapes_per_row):
            x = (-500 + (40 * i * 2.5))
            t.penup()
            t.goto(x,y)
            t.pendown()
            func(t,size)

if __name__ == '__main__':
    win = turtle.Screen()
    BoundingBox.drawBoundingBox()
    t = turtle.Turtle()
    t.speed(10)


    print("Choose an image-drawing function:")
    print("1. drawOneShape")
    print("2. drawOneStar")

    choice = input("Enter the number of the function you want to use: ")
    if choice == "1":
        drawRowsOfRows(t, TurtleShapes.drawOneShape)
    elif choice == "2":
        drawRowsOfRows(t, TurtleShapes.drawOneStar)
    else:
        print("Invalid choice. Please select 1 or 2.")

    win.exitonclick()
    