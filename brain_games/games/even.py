import random

task = 'Answer "yes" if the number is even, otherwise answer.'
    
def engine():
    number = random.randint(1, 100)
    question = number
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question


