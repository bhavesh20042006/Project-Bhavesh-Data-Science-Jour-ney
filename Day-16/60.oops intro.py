import another_module

print(another_module.another_variable)  # This will print 12
import turtle
timmy = turtle.Turtle()


#or
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)  # This will print the Turtle object details
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# Install from a terminal, not inside the script:
# python -m pip install prettytable

from prettytable import PrettyTable
