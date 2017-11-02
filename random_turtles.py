import random
from turtle import *

marc = Turtle()
saleem = Turtle()
fred = Turtle()
teddy = Turtle()
ron = Turtle()

marc.shape("turtle")
marc.color("blue")

saleem.shape("turtle")
saleem.color("red")

fred.shape("turtle")
fred.color("purple")

teddy.shape("turtle")
teddy.color("black")

ron.shape("turtle")
ron.color("orange")

marc.forward(50)

for i in range(10):
    saleem.left(53)
    fred.right(36)
    saleem.forward(11)
    fred.forward(50)
    teddy.right(44)
    ron.right(21)
    teddy.forward(26)
    ron.forward(38)

marc.left(90)

all_turtles = [marc, saleem, fred, teddy, ron]

while True:
    for t in all_turtles:
        rand_dir = random.randint(-20,20)
        rand_dist = random.randint(5,10)

        t.right(rand_dir)
        t.forward(rand_dist)
