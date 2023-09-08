import turtle as t

# Set up the Turtle screen
screen = t.Screen()
screen.bgcolor("red")  # Change the background color to red

# Create a Turtle object
yin_yang = t.Turtle()
yin_yang.speed(0)
yin_yang.penup()
yin_yang.pensize(2)

# Define colors
white_color = "#FFFFFF"
black_color = "#000000"

# Draw the black part of the yin yang symbol
yin_yang.fillcolor(black_color)
yin_yang.goto(0, -200)
yin_yang.begin_fill()
yin_yang.circle(200, 180)
yin_yang.end_fill()

# Draw the white part of the yin yang symbol
yin_yang.fillcolor(white_color)
yin_yang.goto(0, 0)
yin_yang.begin_fill()
yin_yang.circle(200, 180)
yin_yang.end_fill()

# Draw the small black circle
yin_yang.penup()
yin_yang.goto(0, 100)
yin_yang.pendown()
yin_yang.fillcolor(black_color)
yin_yang.begin_fill()
yin_yang.circle(100)
yin_yang.end_fill()

# Hide the Turtle
yin_yang.hideturtle()

# Close the Turtle graphics window when clicked
screen.exitonclick()
