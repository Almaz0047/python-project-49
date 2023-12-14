import brain_games.cli
import prompt


def start(game):
    usname = brain_games.cli.welcome_user()
    correct = 1
    print(game.TASK)
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
            print(f"'{usanswer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {usname}!")
            return
