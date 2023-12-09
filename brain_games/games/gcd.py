import random

task = 'Find the greatest common divisor of given numbers.'


def engine():
    num_one = random.randint(2, 101)
    num_two = random.randint(2, 101)
    question = f'{num_one} {num_two}'
    while num_one != num_two:
        if num_one > num_two:
            num_one = num_one - num_two
        else:
            num_two = num_two - num_one
    correct_answer = str(num_two)
    return correct_answer, question
