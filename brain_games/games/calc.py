import random
from random import randint


TASK = 'What is the result of the expression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 50


def generate_round():
    num_one = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_two = randint(LOWER_LIMIT, UPPER_LIMIT)
    operator = random.choice(['+', '-', '*'])
    correct_answer = str(calculate(num_one, num_two, operator))
    question = f'{num_one} {operator} {num_two}'
    return correct_answer, question


def calculate(num_one, num_two, operator):
    match operator:
        case '+':
            result = num_one + num_two
        case '-':
            result = num_one - num_two
        case '*':
            result = num_one * num_two
    return result
