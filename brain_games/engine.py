import prompt


def run_game(get_answer_and_question, instruction):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(instruction)
    for i in range(3):
        question, correct_answer = get_answer_and_question()
        print("Question:", question)
        answer_user = prompt.string("Your answer: ")
        if answer_user == correct_answer:
            print('Correct!')
        else:
            print(f''''{answer_user}' is wrong answer ;(. Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
