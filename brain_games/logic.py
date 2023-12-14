import brain_games.cli
import prompt

SCORE = 3


def start(game):
    usname = brain_games.cli.welcome_user()
    index = 0
    print(game.TASK)
    while index < SCORE:
        correct_answer, question = game.engine()
        print(f'Question: {question}')
        usanswer = prompt.string('Your answer: ')
        if usanswer == correct_answer:
            print('Correct!')
        else:
            print(f"'{usanswer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {usname}!")
            return
        index += 1
    print(f"Congratulations, {usname}!")
