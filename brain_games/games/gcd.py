from random import randint

TASK = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 2
UPPER_LIMIT = 101


def generate_round():
    num_one = randint(LOWER_LIMIT, UPPER_LIMIT)
    num_two = randint(LOWER_LIMIT, UPPER_LIMIT)
    question = f'{num_one} {num_two}'
    correct_answer = check_divisor(num_one, num_two)
    return correct_answer, question


def check_divisor(num_one, num_two):
    while num_one != num_two:
        if num_one > num_two:
            num_one = num_one - num_two
        else:
            num_two = num_two - num_one
    result = str(num_two)
    return result
