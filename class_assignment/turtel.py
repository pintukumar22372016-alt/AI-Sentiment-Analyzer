import turtle
import time

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("blue")
t.speed(3)        
t.shape("arrow") 
t.pensize(1)

def draw_heart(size):
    t.penup()
    t.goto(0, -size//2)
    t.setheading(140)
    t.pendown()

    t.forward(size)
    t.circle(-size/2, 200)
    t.left(120)
    t.circle(-size/2, 200)
    t.forward(size)
for thickness in range(1, 20):   
    t.pensize(thickness)
    draw_heart(180)
    time.sleep(0.3)
t.pensize(12)
draw_heart(200)

turtle.done()
