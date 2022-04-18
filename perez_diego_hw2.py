import turtle
import colorsys
import time
import math

t = turtle.Turtle()
# t.speed(1)
canvas_width, canvas_height = turtle.screensize()
# turtle.colormode(255)

scale_factor = 10

def fibonacci_turtle(n, scale, tracer):

    l_scale_factor = scale_factor * scale

    n0 = 0
    n1 = 1
    print("[{}, {}]".format(n0, n1))


    if (not tracer):
        turtle.tracer(0)

    t.pendown()

    # Initial square
    t.right(90)
    
    t.forward(l_scale_factor)
    t.left(90)
    t.forward(l_scale_factor)
    t.left(90)
    t.forward(l_scale_factor)
    t.left(90)
    t.forward(l_scale_factor)

    tmp_n0 = n0
    n0 = n1
    n1 = n1 + tmp_n0
    print("[{}, {}]".format(n0, n1))

    for i in range(1, n):
        t.backward(n0 * l_scale_factor)
        t.right(90)

        # if (i == 1):
        #     t.left(90)
        # else:
        #     t.right(90)
        x, y = t.position()
        color_increment = float(1.0 / n)
        rgb_color = colorsys.hls_to_rgb(i * color_increment, 0.5, 1.0)
        # r = int(i * color_increment)
        # g = int(i * color_increment)
        # t.fillcolor(r, g, 0)
        t.fillcolor(rgb_color)
        t.begin_fill()

        t.forward(n1 * l_scale_factor)
        t.left(90)
        t.forward(n1 * l_scale_factor)
        t.left(90)
        t.forward(n1 * l_scale_factor)
        # t.left(90)
        # t.forward(n1 * l_scale_factor)
        # t.left(90)

        t.end_fill()
        t.penup()

        tmp_n0 = n0
        n0 = n1
        n1 = n1 + tmp_n0
        print("[{}, {}]".format(n0, n1))


    # turtle.exitonclick()


def basic_requirements(tracer):

    if (not tracer):
        turtle.tracer(0)

    t.pendown()
    
    # Square
    t.color(255, 0, 0)
    t.begin_fill()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    # t.right(90)
    t.end_fill()

    t.penup()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.pendown()

    # Circle
    t.color(0, 255, 128)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.backward(400)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.pendown()

    # Triangle
    t.color(0, 128, 255)
    t.begin_fill()
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.end_fill()

    t.pendown()



# fibonacci_turtle(16, 1, False)
# turtle.reset()

turtle.colormode(255)

basic_requirements(True)
turtle.exitonclick()