import turtle as t
def lbx(length):
    t.pendown()
    t.begin_fill()
    for i in range(6):
        t.fd(length)
        t.right(60)
    t.end_fill()
    t.penup()

def qiang(x, y):
    t.penup()
    t.goto(x, y)
    for i in range(5):
        lbx(50)
        t.fd(100)

t.setup(800, 800)
t.bgcolor("black")
t.color("black", "yellow")
t.pensize(2)
t.speed(0)
x = -225
y = 300
for i in range(5):
    qiang(x, y)
    y = y - 150
t.hideturtle()
