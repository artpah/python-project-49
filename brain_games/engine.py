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
            a = answer_user
            c = correct_answer
            print(f''''{a}' is wrong answer ;(. Correct answer was '{c}'.
Let's try again, {name}!''')
            return
    print(f'Congratulations, {name}!')
