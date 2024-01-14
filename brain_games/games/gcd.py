from random import randint


import math


from brain_games.engine import run_game


def get_nums_and_gcd():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    nums = f'{num1} {num2}'
    gcd = str(math.gcd(num1, num2))
    return nums, gcd


def run_gcd_game():
    GCD_INSTR = 'Find the greatest common divisor of given numbers.'
    run_game(get_nums_and_gcd, GCD_INSTR)
