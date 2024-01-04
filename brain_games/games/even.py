from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def generate_round():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number


def is_even(number):
    return number % 2 == 0
