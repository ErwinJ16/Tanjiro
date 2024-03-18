import turtle
t=turtle.Turtle()
t.speed(20)
t.penup()
t.goto(-50,0)
t.pendown()
for _ in range(4):
    t.forward(100)
    t.right(90)
t.penup()
t.goto(-200,0)
t.pendown()
for _ in range(3):
    t.forward(100)
    t.right(120)
t.penup()
t.goto(100,0)
t.pendown()
for _ in range(2):
    t.forward(200)
    t.right(90)
    t.forward(70)
    t.right(90)
t.penup()
t.goto(0,150)
t.pendown()
for _ in range(360):
    t.forward(1)
    t.right(1)