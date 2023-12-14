from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 0
UPPER_LIMIT = 30


def engine():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = number
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    if divisor == number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
