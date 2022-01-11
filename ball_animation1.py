import turtle
wn=turtle.Screen()
wn.setup(width=300,height=300)
wn.bgcolor("black")
a =turtle.Turtle()
a.hideturtle()
a.color("blue")
a.up()
a.goto(142,142)
a.down()
a.backward(294)
a.left(90)
a.backward(294)
a.left(90)
a.backward(294)
a.left(90)
a.backward(294)
i= turtle.Turtle()
i.shape("circle")
i.color("green")
i.up()
j= turtle.Turtle()
j.shape("circle")
j.color("yellow")
j.up()
k= turtle.Turtle()
k.shape("circle")
k.color("red")
k.up()
l= turtle.Turtle()
l.shape("circle")
l.color("blue")
l.up()
i.speed(0)
j.speed(0)
k.speed(0)
l.speed(0)
i.dx=2
i.dy=2
j.dx=2
j.dy=-2
k.dx=1
k.dy=-3
l.dx=1
l.dy=1
while True:
	i.setx(i.xcor()+i.dx)
	i.sety(i.ycor()+i.dy)
	j.setx(j.xcor()+j.dx)
	j.sety(j.ycor()+j.dy)
	k.setx(k.xcor()+k.dx)
	k.sety(k.ycor()+k.dy)
	l.setx(l.xcor()+l.dx)
	l.sety(l.ycor()+l.dy)
	if i.ycor()>140:
		i.sety(140)
		i.dy*=-1
	if i.xcor()>140:
		i.setx(140)
		i.dx*=-1
	if i.ycor()<-140:
		i.sety(-140)
		i.dy*=-1
	if i.xcor()<-140:
		i.setx(-140)
		i.dx*=-1
	if j.ycor()>140:
		j.sety(140)
		j.dy*=-1
	if j.xcor()>140:
		j.setx(140)
		j.dx*=-1
	if j.ycor()<-140:
		j.sety(-140)
		j.dy*=-1
	if j.xcor()<-140:
		j.setx(-140)
		j.dx*=-1
	if k.ycor()>140:
		k.sety(140)
		k.dy*=-1
	if k.xcor()>140:
		k.setx(140)
		k.dx*=-1
	if k.ycor()<-140:
		k.sety(-140)
		k.dy*=-1
	if k.xcor()<-140:
		k.setx(-140)
		k.dx*=-1
	if l.ycor()>140:
		l.sety(140)
		l.dy*=-1
	if l.xcor()>140:
		l.setx(140)
		l.dx*=-1
	if l.ycor()<-140:
		l.sety(-140)
		l.dy*=-1
	if l.xcor()<-140:
		l.setx(-140)
		l.dx*=-1