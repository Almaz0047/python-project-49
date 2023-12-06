#!/usr/bin/env python3
import random, prompt


def main():
    print('Welcome to the Brain Games!')   #Знаю, что такой подход неверен, нужно использовать импорты функции из brain_games и cli
    usname = prompt.string('May I have your name? ') 
    #При импорте не получается вернуть значение usname данная функция его не видит из cli,/ 
    #/пробовал вернуть значение через return, но ничего не вышло
    print(f'Hello, {usname}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 1
    while True:
        number = random.randint(1,100)
        print(f'Question: {number}')
        usanswer = prompt.string('Your answer: ') 
        if correct == 3:
            print(f'Congratulations, {usname}!')
            break
        elif number % 2 == 0 and usanswer == 'yes':
            print('Correct!')
            correct += 1
        elif number % 2 == 0 and usanswer != 'yes':
            print(f"Answer '{usanswer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {usname}!")
            break
        elif number % 2 != 0 and usanswer == 'no':
            print('Correct!')
            correct += 1
        elif number % 2 != 0 and usanswer != 'no':
            print(f"Answer '{usanswer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {usname}!")
            break


if __name__ == '__main__':
    main()
