import random
from brain_games.engine import run_game
from brain_games.games.constants import PROGRESSION_INSTRUCTION


def get_prog_and_missed_elem():
    start = random.randint(1, 100)
    step = random.randint(1, 100)
    length = random.randint(5, 10)
    prog_list = list(range(start, start + step * length, step))
    random_index = random.randint(0, len(prog_list) - 1)
    random_elem = prog_list[random_index]
    prog_list[random_index] = '..'
    prog = ' '.join(map(str, prog_list))
    return prog, str(random_elem)


def run_progression_game():
    run_game(get_prog_and_missed_elem, PROGRESSION_INSTRUCTION)
