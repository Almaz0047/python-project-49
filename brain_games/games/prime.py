import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def engine():
    number = random.randint(0, 30)
    question = number
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    if divisor == number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question
