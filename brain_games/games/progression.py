from random import randint

TASK = 'What number is missing in the progression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 20
MIN_LENGHT = 5
MAX_LENGHT = 12
MIN_STEP = 2
MAX_STEP = 5


def engine():
    start = randint(LOWER_LIMIT, UPPER_LIMIT)
    step = randint(MIN_STEP, MAX_STEP)
    length = randint(MIN_LENGHT, MAX_LENGHT)
    progression = get_progression(start, step, length)
    index_num = randint(1, len(progression) - 1)
    correct_answer = str(progression[index_num])
    progression[index_num] = '..'
    question = ' '.join(map(str, progression))
    return correct_answer, question


def get_progression(start, step, length):
    end = start + (length * step)
    num_list = []
    for index in range(start, end, step):
        num_list.append(index)
    return num_list
