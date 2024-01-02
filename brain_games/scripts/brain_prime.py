#!/usr/bin/env python3
from random import randint


import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('"yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1,100)
        def is_prime(num):
            if num < 2:
                return 'no'
            for i in range(2, int(num ** 0.5)+1):
                if num % i == 0:
                   return 'no'
            return 'yes'
        print(f'Question: {num}')

        answer_user = prompt.string("Your answer: ")

        if (is_prime(num) == 'yes' and answer_user == 'yes') or (is_prime(num) == 'no' and answer_user == 'no'):
            print('Correct!')
            i += 1
        else:
            print(f''''{answer_user}' is wrong answer ;(. Correct answer was '{is_prime(num)}'. Let's try again, {name} ''')
            break
    else:
        print(f'Congratulations, {name}!')
if __name__ == '__main__':
    main()
