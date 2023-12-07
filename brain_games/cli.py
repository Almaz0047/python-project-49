import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    usname = prompt.string('May I have your name? ')
    print(f'Hello, {usname}!')
    return usname
