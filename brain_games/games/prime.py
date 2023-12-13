import random

task = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def engine():
    number = random.randint(0, 25)
    prime_check = number / 9
    question = number
    if prime_check <= 1:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question