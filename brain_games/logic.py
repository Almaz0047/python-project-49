import cli
import prompt


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
        elif usanswer == correct_answer:
            print('Correct!')
            correct += 1
        else:
            print(f"Answer '{usanswer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {usname}!")
            break
