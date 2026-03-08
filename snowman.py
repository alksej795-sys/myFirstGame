import turtle

t = turtle.Turtle()
t.speed(5)

def circle(x, y, r):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)

# Нижний шар
circle(0, -150, 100)

# Средний шар
circle(0, -20, 70)

# Голова
circle(0, 90, 50)

# Глаза
circle(-15, 150, 5)
circle(15, 150, 5)

# Нос (морковка)
t.penup()
t.goto(0, 140)
t.pendown()
t.color("orange")
t.begin_fill()
for _ in range(3):
    t.forward(20)
    t.left(120)
t.end_fill()

turtle.done()
