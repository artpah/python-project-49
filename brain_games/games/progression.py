import random
from brain_games.engine import run_game
from brain_games.constants import PROGRESSION_INSTRUCTION, MIN_LEN, MAX_LEN


def get_prog_and_missed_elem():
    start, step = random.randint(1, 100), random.randint(1, 100)
    length = random.randint(MIN_LEN, MAX_LEN)
    prog_list = list(range(start, start + step * length, step))
    random_index = random.randint(0, len(prog_list) - 1)
    missed_num = prog_list[random_index]
    prog_list[random_index] = '..'
    prog = ' '.join(map(str, prog_list))
    return prog, str(missed_num)


def run_progression_game():
    run_game(get_prog_and_missed_elem, PROGRESSION_INSTRUCTION)
