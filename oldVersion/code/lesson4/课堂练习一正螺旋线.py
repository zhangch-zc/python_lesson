import turtle as t
t.setup(800, 800,)
t.bgcolor("black")
t.pensize(1)
t.pencolor("yellow")
t.speed(10)
a = 1
for x in range(100):
    a = a + 2
    t.right(90)
    t.fd(a)
t.done()
