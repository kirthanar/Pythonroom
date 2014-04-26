# author: kirthanar

import turtle

length = 100
angle = 90
#numbers= range(0,6)
colors = ["red", "blue", "green", "yellow"]

kirthana = turtle.Turtle()

for color in colors:
	kirthana.color(color)
	kirthana.forward(length)
	kirthana.left(angle)
