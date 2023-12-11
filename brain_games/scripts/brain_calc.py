#!/usr/bin/env python3
from random import randint, choice


import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    i = 0
    while i < 3:
        num1 = randint(0, 100)
        num2 = randint(0, 100)
        op = choice(['+', '-', '*'])

        print(f'Question: {num1} {op} {num2}')

        answer_user = prompt.string("Your answer: ")
        result = eval(f'{num1} {op} {num2}')
        if answer_user == str(result):
            print('Correct!')
            i += 1
        else:
            print(f''''{answer_user.lower()}' is wrong answer ;(. Correct answer was '{result}'.
Let's try again, {name} ''')
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
