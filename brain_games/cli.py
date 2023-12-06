import prompt


def welcome_user():
    usname = prompt.string('May I have your name? ')
    print(f'Hello, {usname}!')
