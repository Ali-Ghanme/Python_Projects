import turtle
from turtle import *
frow = 1
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
while True:
    for colours in ["red" , "magenta" , "blue" ,"cyan" ,"green","yellow","white"]:
     t.color(colours)
     t.forward(frow)
     t.left(90)
     t.left(1)
     frow += 1
     turtle.hideturtle()
