import turtle

def draw_k(some_turtle, x, y):
    some_turtle.up()
    some_turtle.goto(x,-y)
    some_turtle.down()
    some_turtle.goto(x,y)
    some_turtle.goto(x,0)
    some_turtle.right(40)
    some_turtle.forward(200)
    some_turtle.goto(x,0)
    some_turtle.left(80)
    some_turtle.forward(200)

def draw_c(some_turtle, x, y):
    some_turtle.forward(150)
    some_turtle.goto(x,y)
    some_turtle.goto(x,-y)
    some_turtle.forward(150)
    

def draw_path():
    windows = turtle.Screen()
    windows.bgcolor('white')
    # Create the turtle line - draw line
    line = turtle.Turtle()
    line.shape('turtle')
    line.color('blue')
    line.speed(0)
    draw_k(line, -125, 150)
    line.up()
    line.goto(125, 150)
    line.down()
    line.right(40)
    draw_c(line,125, 150)

    windows.exitonclick()

draw_path()
