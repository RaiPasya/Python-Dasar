import turtle

t = turtle.Turtle()

def fibonacci_tree(t, branch_length, level, angle):
    if level > 0:
        t.color("brown")
        t.pensize(4)
        t.forward(branch_length)

        pos = t.pos()
        heading = t.heading()

        t.left(angle)
        fibonacci_tree(t, branch_length * 0.7, level - 1, angle)

        
        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()

        t.right(angle * 2)
        fibonacci_tree(t, branch_length * 0.7, level - 1, angle)

        t.penup()
        t.setpos(pos)
        t.setheading(heading)
        t.pendown()

t.left(90) 
t.penup()
t.goto(0, -200)
t.pendown()

fibonacci_tree(t, 100, 7, 30)

turtle.done()
