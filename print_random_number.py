import random


def print_random_number():
    number = random.randint(1, 10)
    if number == 3:
        return 'three'
    elif number == 5:
        return 'five'
