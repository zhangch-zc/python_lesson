import turtle as t
t.setup(800, 800)
t.bgcolor("black")
t.speed(10)
t.pensize(5)
t.color("yellow", "red")
t.begin_fill()
t.up()
t.goto(-300, 0)
t.down()
t.fd(600)
t.right(90)
t.fd(300)
t.right(90)
t.fd(600)
t.right(90)
t.fd(300)
t.goto(0, 300)
t.goto(300, 0)
t.end_fill()
t.hideturtle()
