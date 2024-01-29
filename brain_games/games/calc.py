import random
from brain_games.engine import run_game
from brain_games.constants import CALC_INSTRUCTION


def get_math_exp_and_res():
    num1, num2 = random.randint(0, 100), random.randint(0, 100)
    op1, op2, op3 = '+', '-', '*'
    op = random.choice([op1, op2, op3])
    exp = f'{num1} {op} {num2}'
    result_calc = eval(exp)
    return exp, str(result_calc)


def run_calc_game():
    run_game(get_math_exp_and_res, CALC_INSTRUCTION)
