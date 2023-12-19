from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 0
UPPER_LIMIT = 30


def generate_round():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = number
    if check_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def check_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number