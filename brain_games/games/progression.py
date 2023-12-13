import random

task = 'What number is missing in the progression?'


def engine():
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 12)
    progression = get_progression(start, step, length)
    index_num = random.randint(1, len(progression) - 1)
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
