import turtle
tur=turtle.Turtle()

turtle.setup(750,750)


tur.fillcolor(0,0,1)
tur.begin_fill()
for i in range(360):
    tur.forward(50)
    tur.right(1)
for i in range(12):
    tur.forward(50)
    tur.left(30)
tur.end_fill()
turtle.done()
turtle.exitonclick()