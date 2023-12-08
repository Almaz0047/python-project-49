import random

task = 'What is the result of the expression?'

def engine():
    num_one = random.randint(1, 50)
    num_two = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    correct_answer = str(calculator(num_one, num_two, operator))
    question = f'{num_one} {operator} {num_two}'
    return correct_answer, question


def calculator(num_one, num_two, operator):
    if operator == '+':
        result = num_one + num_two
    elif operator == '-':
        result = num_one - num_two
    elif operator == '*':
        result = num_one * num_two
    return result