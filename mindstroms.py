import turtle


def draw_square(some_turtle):
    # move forward and turn right makes these steps four times
    for i in range(4):
        some_turtle.forward(100)
        some_turtle.right(90)
    


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    #Create the turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow','green')
    brad.speed(0)
    for i in range(36):
      draw_square(brad)
      brad.right(10)

    '''#Create the turtle Angie - Draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    '''

    window.exitonclick()


draw_art()
