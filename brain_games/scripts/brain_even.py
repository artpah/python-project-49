#!/usr/bin/env python3
import prompt


from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        number = randint(0, 100)
        def is even(number):
            if number % 2 == 0:
                return "yes"
            else:
                return "no"


        print("Question:", number)

        answer_user = prompt.string("Your answer: ")

        if (is even(number) == "yes" and answer_user == "yes") or (is even(number) == "no" and ansver_user == "no"):
            print('Correct!')
            i += 1
        else:
            print(f''''{ansver_user}' is wrong answer ;(. Correct answer was '{is even(number)}'.
Let's try again, {name} ''')
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
