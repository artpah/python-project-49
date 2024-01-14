from random import randint


from brain_games.engine import run_game


def get_num_and_res():
    num = randint(0, 100)
    res = 'yes' if num % 2 == 0 else 'no'
    return num, res


def run_even_game():
    EVEN_INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(get_num_and_res, EVEN_INSTRUCTION)
