import prompt


def run_game(get_answer_and_question, instruction):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{instruction}')
    repeat_correct_answer = 3
    for i in range(repeat_correct_answer):
        question, correct_answer = get_answer_and_question()
        answer_user = prompt.string(f'Question: {question}\n'
                                    'Your answer: ')
        if answer_user == correct_answer:
            print('Correct!')
        else:
            print(f"{answer_user} is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
