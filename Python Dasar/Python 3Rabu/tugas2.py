import turtle

window = turtle.Screen()

def drawSquare(ttl, x, y, length, width):
    ttl.penup()
    ttl.fillcolor("red")
    ttl.begin_fill()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
    ttl.end_fill()
    ttl.penup()

def drawTriangle(ttl, x, y, length):
    ttl.penup()
    ttl.fillcolor("yellow")
    ttl.begin_fill()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(3):
        ttl.forward(length)
        ttl.left(120)
    ttl.end_fill()
    ttl.penup()

def drawJa(ttl, x, y, length, width):
    ttl.penup()
    ttl.fillcolor("green")
    ttl.begin_fill()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(130)
        ttl.forward(width)
        ttl.left(50)
    ttl.end_fill()
    ttl.penup()

def drawTrapezoid(ttl, x, y, length, width):
    ttl.penup()
    ttl.fillcolor("blue")
    ttl.begin_fill()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(120)
        ttl.forward(width)
        ttl.left(60)
    ttl.end_fill()
    ttl.penup()

def drawPentagon(ttl, x, y, size):
    ttl.penup()
    ttl.fillcolor("purple")
    ttl.begin_fill()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(5):
        ttl.forward(size * 1)
        ttl.left(72)
    ttl.end_fill()
    ttl.penup()

Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)

drawSquare(Bob, 0, 0, 150, 100)
drawTriangle(Bob, 0, 150, 150)
drawJa(Bob, 0, -150, 150, 75)
drawTrapezoid(Bob, 300, 0, 200, 100)
drawPentagon(Bob, -300, 0, 150)

window.exitonclick()
