import turtle
tur=turtle.Turtle()

#設置畫面大小↓
turtle.setup(850,850)

def retangle():
    tur.begin_fill()
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.end_fill()
def myGoto(x,y):    
    tur.penup()
    tur.goto(x,y)    
    tur.pendown()

myGoto(-400,400)
tur.fillcolor(0,0,0)
retangle()
myGoto(-400,200)
tur.fillcolor(1,0,0)
retangle()
myGoto(-400,0)
tur.fillcolor(1,1,0)
retangle()

turtle.done()
turtle.exitonclick()