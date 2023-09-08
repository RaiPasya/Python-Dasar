import turtle

# Membuat layar untuk menggambar
wn = turtle.Screen()
wn.bgcolor("white")

# Membuat objek turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(10)

# Membuat bentuk bunga
def draw_flower():
    for _ in range(36):
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(135)
        flower.forward(100)
        flower.right(45)
        flower.forward(100)
        flower.right(135)
        flower.right(10)

# Menggambar bunga
flower.penup()
flower.goto(0, -150)
flower.pendown()
draw_flower()

# Menutup layar saat diklik
wn.exitonclick()
