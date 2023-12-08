import random, prompt, cli


def main():
    usname = cli.welcome_user()
    print('What is the result of the expression?')
    i = 1
    while True:
        num_one = random.randint(1, 50)
        num_two = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        print(f'Question: {num_one} {operator} {num_two}')
        usanswer = prompt.string('Your answer: ')
        if i == 3:
            print(f'Congratulations! {usname}')
            break
        elif usanswer == str(calculator(num_one, num_two, operator)):
            print('Correct!')
            i += 1
        else:
            print(f"{usanswer} is wrong answer ;(. "
                f"Correct answer was '{str(calculator(num_one, num_two, operator))}'")
            print(f"Let's try again, {usname}")
            break


def calculator(num_one, num_two, operator):
    if operator == '+':
        result = num_one + num_two
    elif operator == '-':
        result = num_one - num_two
    elif operator == '*':
        result = num_one * num_two
    return result


if __name__ == '__main__':
    main()