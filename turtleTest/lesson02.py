import turtle as t

t.pensize(9)
t.color('black')
t.circle(75)

t.penup()
t.goto(-180,0)
t.pendown()

t.color('blue')
t.circle(75)

t.penup()
t.goto(180,0)
t.pendown()

t.color('red')
t.circle(75)

t.penup()
t.goto(80,-100)
t.pendown()

t.color('green')
t.circle(75)

t.penup()
t.goto(-80,-100)
t.pendown()

t.color('yellow')
t.circle(75)

t.penup()
t.goto(-100,180)
t.pendown()
t.color('black')
t.write('北京 2020', font = ('kaiti', 32))
