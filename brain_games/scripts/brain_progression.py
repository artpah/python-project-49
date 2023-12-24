#!/usr/bin/env python3
from random import randint, choice


import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    i = 0
    while i < 3:
        start = randint(1, 100)
        step = randint(1, 100)
        length = randint(5, 10)
        prog = list(range(start, start + step * length, step))
        random_elem = choice(prog)
        index = prog.index(random_elem)
        prog[index] = '..'
        prog = ' '.join(map(str, prog))

        print(f'Question: {prog}')

        answer_user = prompt.string("Your answer: ")
        if answer_user == str(random_elem):
          print('Correct!')
          i += 1
        else:
          print(f''''{answer_user.lower()}' is wrong answer ;(. Correct answer was '{random_elem}'.
Let's try again, {name} ''')
          break
    else:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
