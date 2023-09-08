import turtle

window = turtle.Screen()

def drawSquare(ttl, x, y, length):
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(0)
    ttl.pendown()
    for _ in range(4):
        ttl.forward(length)
        ttl.left(90)
    ttl.penup()

Bob = turtle.Turtle()
Bob.speed(10)
Bob.pensize(3)
drawSquare(Bob, 0, 0, 100)
window.exitonclick()
