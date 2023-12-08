import cli, prompt


def start(game):
    usname = cli.welcome_user()
    correct = 1
    print(game.task)
    while True:
        correct_answer, question = game.engine()
        print(f'Question: {question}')
        usanswer = prompt.string('Your answer: ')
        if correct == 3:
            print(f'Congratulations! {usname}')
            break
        if usanswer == correct_answer:
            print(f'Correct!')
            correct += 1
        else:
            print(f"Answer '{usanswer}' is wrong answer ;(. "
            f"Correct answer was '{correct_answer}'.\nLet's try again, {usname}!")
            break