from random import randint, choice


from brain_games.engine import run_game


def get_prog_and_random_elem():
    start = randint(1, 100)
    step = randint(1, 100)
    length = randint(5, 10)
    prog_list = list(range(start, start + step * length, step))
    random_elem = choice(prog_list)
    index = prog_list.index(random_elem)
    prog_list[index] = '..'
    prog = ' '.join(map(str, prog_list))
    random_elem = str(random_elem)
    return prog, random_elem


def run_progression_game():
    PROGR_INSTR = 'What number is missing in the progression?'
    run_game(get_prog_and_random_elem, PROGR_INSTR)
