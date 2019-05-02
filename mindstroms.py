import turtle


def draw_square():
    # move forward and turn right makes these steps four times
    
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow','green')
    brad.speed(2)
    for i in range(4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    # draw circle with turtle library
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    


window = turtle.Screen()
window.bgcolor("red")
draw_square()
draw_circle()
window.exitonclick()
