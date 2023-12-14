from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def engine():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
