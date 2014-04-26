# author: kirthanar

import turtle


sides=15
length = 35
angle = 180-180*(sides -2) /sides 
numbers= range(0,sides)
#colors = ["red", "blue", "green", "yellow"]

kirthana = turtle.Turtle()

for number in numbers:
	
	kirthana.forward(length)
	kirthana.left(angle)
