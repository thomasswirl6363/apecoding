import turtle
tur=turtle.Turtle()

#設置畫面大小↓
turtle.setup(850,850)

def retangle():
    tur.begin_fill()
    tur.forward(600)
    tur.right(90)
    tur.forward(400)
    tur.right(90)
    tur.forward(600)
    tur.right(90)
    tur.forward(400)
    tur.right(90)
    tur.end_fill()
def myGoto(x,y):    
    tur.penup()
    tur.goto(x,y)    
    tur.pendown()

myGoto(-400,400)
tur.fillcolor(0,0,1)
retangle()
myGoto(-400,240)
tur.fillcolor(1,1,0)
tur.begin_fill()
tur.forward(600)
tur.right(90)
tur.forward(70)
tur.right(90)
tur.forward(600)
tur.right(90)
tur.forward(70)
tur.end_fill()

myGoto(-200,400)
tur.fillcolor(1,1,0)
tur.begin_fill()
tur.right(90)
tur.forward(75)
tur.right(90)
tur.forward(400)
tur.right(90)
tur.forward(75)
tur.right(90)
tur.forward(400)
tur.end_fill()

turtle.done()
turtle.exitonclick()