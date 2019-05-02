import turtle


def draw_square():
    # move forward and turn right makes these steps four times
    window = turtle.Screen()
    window.bgcolor("red")


    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow','green')
    brad.speed(2)

    for i in range(4):
        brad.forward(100)
        brad.right(90)


    window.exitonclick()

draw_square()
