from turtle import *

#we wanna paint a house
speed(30)

width(7)
color("brown")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#door
forward(70)
left(90)
color("black")
begin_fill()


forward(120)
right(90)

forward(60)
right(90)

forward(120)
end_fill()
 
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(10,130)
pendown()


# drawing 1st window
color("grey")
begin_fill()
left(120)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

#drawing 2nd window
penup()
goto(190,130)
pendown()

color("grey")
begin_fill()
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()