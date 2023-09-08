import turtle

window = turtle.Screen()

def drawSquare(ttl, x, y, length, width):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(90)
        ttl.forward(width)
        ttl.left(90)
    ttl.penup()

def drawTriangle(ttl, x, y, length):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(3):
        ttl.forward(length)
        ttl.left(120)
    ttl.penup()

def drawJa(ttl, x, y, length, width):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(2):
        ttl.forward(length)
        ttl.left(130)
        ttl.forward(width)
        ttl.left(50)
    ttl.penup()

def drawTrapezoid(ttl, x, y, length, width):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(1):
        ttl.forward(length)
        ttl.left(120)
        ttl.forward(width)
        ttl.left(60)
        ttl.forward(width)
        ttl.left(60)
        ttl.forward(width)
    ttl.penup()

def drawRhombus(ttl, x, y, diagonal_length):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(45)
    ttl.pendown()
    for _ in range(4):
        ttl.forward(diagonal_length)
        ttl.right(90)
    ttl.penup()

Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)
drawSquare(Bob, 0, 0, 150, 100)
drawTriangle(Bob, 0, 150, 150)
drawJa(Bob, 0, -150, 150, 75)
drawTrapezoid(Bob, 300, 0, 200, 100,)
drawRhombus(Bob, 300, -150, 100)

window.exitonclick()
