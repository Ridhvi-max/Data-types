import turtle
screen = turtle.Screen()
pen = turtle.Turtle()
pen.pensize(3)       
pen.color("blue")      
for _ in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()