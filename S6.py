# updated code
import random
import turtle

myturtle = turtle.Turtle()
screen = turtle.Screen()
arColors = ["deepskyblue", "skyblue", "lightblue", "powderblue", "lightsteelblue"]
xpixels = screen.window_width()//2
ypixels = screen.window_height()//2
myturtle.speed(0)

def makeArm(intScale):
    myturtle.forward(20*intScale)
    myturtle.left(45)
    myturtle.forward(10*intScale)
    myturtle.right(90)
    myturtle.forward(2*intScale)
    myturtle.right(90)
    myturtle.forward(8*intScale)
    myturtle.left(135)
    myturtle.forward(10*intScale)
    myturtle.right(90)
    myturtle.forward(2*intScale)
    myturtle.right(90)
    myturtle.forward(10*intScale)
    myturtle.left(135)
    myturtle.forward(8*intScale)
    myturtle.right(90)
    myturtle.forward(2*intScale)
    myturtle.right(90)
    myturtle.forward(10*intScale)
    myturtle.left(45)
    myturtle.forward(20*intScale)

while True:
    xColor = random.choice(arColors)
    myturtle.pencolor(xColor)
    myturtle.fillcolor(xColor)
    myturtle.penup()
    xloc = random.randint(-1*xpixels,xpixels)
    yloc = random.randint(-1*ypixels,ypixels)
    myturtle.goto(xloc,yloc)
    myturtle.pendown()
    intScale2 = random.randint(1,10)/5
    myturtle.begin_fill()
    for x in range(9):
        myturtle.left(140)
        makeArm(intScale2)
    myturtle.end_fill()
