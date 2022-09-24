import turtle as t

def zfx(length):
    t.pendown()
    t.begin_fill()
    for x in range(4):
        t.fd(length)
        t.right(90)
    t.end_fill()
    t.penup()

def qiang(x, y):
    t.penup()
    t.goto(x, y)
    for x in range(10):
        zfx(100)
        t.fd(100)


t.speed(0)
t.color("black", "red")
t.penup()
x = -500
y = 500
for i in range(5):
    qiang(x, y)
    y = y - 150
t.done()
