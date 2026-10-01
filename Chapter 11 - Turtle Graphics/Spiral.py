import turtle

t = turtle.Turtle()

t.speed(0)
t.pensize(2)

distance = 1

while True:
    t.forward(distance)
    t.right(91)

    distance += 1

turtle.done()