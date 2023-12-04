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
        print("Question:", number)

        answer_user = prompt.string("Your answer: ")

        if (number % 2 == 0 and answer_user.lower() == "yes") or (number % 2 != 0 and answer_user.lower() == "no"):
            print('Correct!')
            i += 1
        else:
            print(f''''yes' is wrong answer ;(. Correct answer was 'no'. 
Let's try again, {name} ''')
            break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
