'''
DrawRandom.py

@author: christiankirby
'''
import random
import turtle
import BoundingBox
import TurtleShapes



def drawEverywhere(turtle, draw_function):
    """
    A function that draws a shape at a random spot"
    """
    numShapes = int(input('How many shapes to draw? '))
    for _ in range(numShapes):
            x = random.randint(-200, 200)  # Random x-coordinate (adjust as needed)
            y = random.randint(-200, 200)  # Random y-coordinate (adjust as needed)
            size = random.randint(20, 100)  # Random size (adjust as needed)

            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            draw_function(turtle, size)


if __name__ == '__main__':
    win = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    BoundingBox.drawBoundingBox()

    print("Choose an image-drawing function:")
    print("1. drawOneShape")
    print("2. drawOneStar")

    choice = input("Enter the number of the function you want to use: ")


    if choice == "1":
        drawEverywhere(t, TurtleShapes.drawOneShape)
    elif choice == "2":
        drawEverywhere(t, TurtleShapes.drawOneStar)
    else:
        print("Invalid choice. Please select 1 or 2.")

    win.exitonclick()
    