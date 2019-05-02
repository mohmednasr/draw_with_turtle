import turtle
import math
def draw_triangle(some_turtle):
    some_turtle.forward(100)
    some_turtle.left(90)
    some_turtle.forward(100)
    some_turtle.left(135)
    some_turtle.forward(100*math.sqrt(2))
    some_turtle.left(135)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')
    # Create the turtle lite -- draw a triangle
    lite = turtle.Turtle()
    lite.shape('turtle')
    lite.color('blue')
    lite.speed(0)
    for i in range(36):
        draw_triangle(lite)
        lite.right(10)
    lite.right(90)
    lite.forward(300)


    window.exitonclick()

draw_art()
