import turtle as t

def zfx(length):
    t.pendown()
    for x in range(4):
        t.fd(length)
        t.right(90)
    t.penup()
    
t.speed(8)
t.color("black", "red")
t.begin_fill()
t.penup()
t.goto(-500, 0)
for x in range(10):
    zfx(100)
    t.fd(100)
t.end_fill()
t.done()
