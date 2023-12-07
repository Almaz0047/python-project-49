import random, prompt, cli


def main():
    usname = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct = 1
    while True:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        usanswer = prompt.string('Your answer: ')
        if correct == 3:
            print(f'Congratulations, {usname}!')
            break
        elif number % 2 == 0 and usanswer == 'yes' or number % 2 != 0 and usanswer == 'no':
            print('Correct!')
            correct += 1
        elif number % 2 == 0 and usanswer != 'yes':
            print(f"Answer '{usanswer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {usname}!")
            break
        elif number % 2 != 0 and usanswer != 'no':
            print(f"Answer '{usanswer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {usname}!")
            break


if __name__ == '__main__':
    main()