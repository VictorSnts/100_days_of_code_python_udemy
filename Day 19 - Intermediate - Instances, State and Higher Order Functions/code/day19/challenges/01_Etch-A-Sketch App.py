import turtle as t

turtle = t.Turtle()
screen = t.Screen()


def move_forwards():
    turtle.forward(10)


def turn_right():
    turtle.right(10)


def turn_left():
    turtle.left(10)


def move_back():
    turtle.forward(-10)


def reset():
    turtle.home()
    turtle.clear()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='c', fun=reset)
screen.exitonclick()
