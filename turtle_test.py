import turtle
tur=turtle.Turtle()

turtle.setup(750,750)

tur.penup()
tur.goto(-350,350)
tur.pendown()
tur.fillcolor(0,0,1)
tur.begin_fill()
for i in range(4):
    tur.forward(100)
    tur.right(90)
for i in range(8):
    tur.forward(30)
    tur.right(45)
for i in range(3):
    tur.right(25)
    tur.forward(150)
for i in range(360):
    tur.right(1)
    tur.forward(1)
for i in range(3):
    tur.right(160)
    tur.forward(150)
for i in range(4):
    tur.right(80)
    tur.forward(150)
for i in range(72):
    tur.left(5)
    tur.forward(30)
tur.end_fill()
turtle.done()
turtle.exitonclick()