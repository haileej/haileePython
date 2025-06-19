import turtle
myTurtle = turtle.Turtle()

intLen = 100
intSides = 10
intAngle = 360 / intSides

turtle.begin_fill()
for x in range(intSides):
    turtle.forward(intLen)
    turtle.right(intAngle)
turtle.end_fill()

screen = turtle.Screen()
screen.exitonclick()

