import turtle
myturtle = turtle.Turtle()
# ##### Setup Section #######

myturtle.speed(9)
intPetalsTotal = 6
intAngle = 360 // intPetalsTotal
intPetalsDrawn = 0
intDotSize = 25
# ##### END Setup Section #######

# ##### START Loop to Draw Petals #######
while (intPetalsDrawn <= intPetalsTotal):
    myturtle.fillcolor("#b380ff")
    myturtle.begin_fill()
    # Draw a circle segment with a 200 radius, but only for 40 degrees
    myturtle.circle(200, 45)
    # Draw a circle segment with a radius of 10, for 140 degrees
    myturtle.circle(10, 140)
    # Repeat the two lines above, to complete
    # 360 degrees and end up back at the start.
    myturtle.circle(200, 45)
    myturtle.circle(10, 140)
    myturtle.end_fill()
    myturtle.right(intAngle)
    intPetalsDrawn += 1
# ##### END Loop to Draw Petals #######

##### START Drawing the center of the flower #######
myturtle.forward(intDotSize-7)
myturtle.left(100)
myturtle.fillcolor("#EEEE77")
myturtle.begin_fill()
myturtle.circle(intDotSize, steps = 8)
myturtle.end_fill()
##### END Drawing the center of the flower #######

# Finish up
screen = turtle.Screen()
screen.exitonclick()