import random

colors = [
    "black",
    "blue",
    "brown",
    "cyan",
    "darkblue",
    "grey",
    "magenta",
    "orange",
    "purple",
    "red",
    "violet",
    "yellow"
]


def get_color():
    choice = random.choice(colors)
    colors.remove(choice)
    return choice

