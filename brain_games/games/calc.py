from random import randint, choice


from brain_games.engine import run_game


def get_exp_and_res():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    op = choice(['+', '-', '*'])
    exp = f'{num1} {op} {num2}'
    res = str(eval(exp))
    return exp, res


def run_calc_game():
    CALC_INSTR = 'What is the result of the expression?'
    run_game(get_exp_and_res, CALC_INSTR)
