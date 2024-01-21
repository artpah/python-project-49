import random
from brain_games.engine import run_game
from brain_games.games.constants import EVEN_INSTRUCTION


def get_num_and_even_ans():
    num = random.randint(0, 100)
    even_ans = 'yes' if num % 2 == 0 else 'no'
    return num, even_ans


def run_even_game():
    run_game(get_num_and_even_ans, EVEN_INSTRUCTION)
