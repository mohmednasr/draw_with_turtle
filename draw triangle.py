import turtle
import math

def draw_small_tri(some_turtle,l):
    some_turtle.fillcolor('green')
    some_turtle.begin_fill()
    for i in range(3):
        some_turtle.forward(l)
        some_turtle.left(120)
    some_turtle.end_fill()

def draw_tri(some_tur, l , x, y):
    draw_small_tri(some_tur,l)
    some_tur.goto(x + l*math.cos(math.pi/3), y + l*math.sin(math.pi/3))
    draw_small_tri(some_tur,l)
    some_tur.goto(x+ l, y+ 0)
    draw_small_tri(some_tur,l)
    

def draw_big_tri(some, l, x, y):
    some.goto(x,y)
    draw_tri(some,l, x, y)
    some.goto(x,y)
    some.goto(x + 2*l*math.cos(math.pi/3), y + 2*l*math.sin(math.pi/3))
    draw_tri(some,l, x + 2*l*math.cos(math.pi/3), y + 2*l*math.sin(math.pi/3))
    some.goto(x + 2*l*math.cos(math.pi/3), y + 2*l*math.sin(math.pi/3))
    some.goto(x + 2*l, y + 0)
    draw_tri(some,l, x + 2*l, y + 0)



def draw_graph(l=20):
    window = turtle.Screen()
    window.bgcolor('white')
    # Create the turtle lite - draw a triangle
    lite = turtle.Turtle()
    lite.shape('turtle')
    lite.color('yellow')
    lite.speed(0)
    draw_big_tri(lite,l,0,0)
    lite.goto(0,0)
    draw_big_tri(lite,l,4*l*math.cos(math.pi/3), 4*l*math.sin(math.pi/3))
    lite.goto(4*l*math.cos(math.pi/3), 4*l*math.sin(math.pi/3))
    draw_big_tri(lite,l,4*l,0)
    window.exitonclick()

    

draw_graph(30)
