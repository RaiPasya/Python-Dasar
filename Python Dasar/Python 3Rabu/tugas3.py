import turtle

window = turtle.Screen()
window.bgcolor("black")

def drawSquare1(ttl, x, y, length, width, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
    ttl.end_fill()
    ttl.penup()

def drawSquare2(ttl, x, y, length, width, color):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    ttl.fillcolor(color)
    ttl.begin_fill()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
    ttl.end_fill()
    ttl.penup()


Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)
drawSquare1(Bob, 0, 0, 200, 50, "red")
drawSquare2(Bob, 0, -50, 200, 50, "white")

window.exitonclick()