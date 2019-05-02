import turtle

def draw_small_tri(some_turtle,l):
    some_turtle.fillcolor('green')
    some_turtle.begin_fill()
    for i in range(3):
        some_turtle.forward(l)
        some_turtle.left(120)
    some_turtle.end_fill()

def draw_tri(some_tur,l):
    draw_small_tri(some_tur,l)
    some_tur.forward(l)
    draw_small_tri(some_tur,l)
    some_tur.forward(l)
    some_tur.left(120)
    some_tur.forward(l)
    draw_small_tri(some_tur,l)

def draw_big_tri(some,l):
    draw_tri(some,l)
    #
    some.forward(l)
    some.right(120)
    #
    draw_tri(some,l)
    #
    some.right(180)
    some.forward(l*2+l)
    some.right(120)
    some.forward(l*2)
    some.right(180)
    #
    draw_tri(some,l)


def draw_graph(l=20):
    window = turtle.Screen()
    window.bgcolor('white')
    # Create the turtle lite - draw a triangle
    lite = turtle.Turtle()
    lite.shape('turtle')
    lite.color('yellow')
    lite.speed(10)
    for i in range(1):
        draw_big_tri(lite,l)

        lite.forward(l*3)
        lite.right(120)

        draw_big_tri(lite,l)

        lite.right(180)
        lite.forward(l*5)
        lite.right(120)
        lite.forward(l*4)
        lite.right(180)

        draw_big_tri(lite,l)

    window.exitonclick()

draw_graph(30)
