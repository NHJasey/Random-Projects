import turtle

def draw_square():
	for i in range(1,5):
	some_turtle.forward(100)
	some_turtle.right(90)
	
def draw_art():
	window = turtle.Screen()
	window.bgcolor("red")
	
	
	rex = turtle.Turtle()
	rex.shape("arrow")
	rex.color("blue")
	red.speed(1)
	for i in range(1,37):
		draw_square(rex)
		rex.right(10)
	
	slinky = turtle.Turtle()
	slinky.shape("turtle")
	slinky.color("green")
	slinky.circle(20)
	
	window.exitonclick()

draw_art()
