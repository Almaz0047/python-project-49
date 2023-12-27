from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 0
UPPER_LIMIT = 54


def generate_round():
    number = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = number
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


def is_prime(number):
    divisor = 2
    if number < 2:
        return False
    else:
        while number % divisor != 0:
            divisor += 1
    return divisor == number
