import random
import math
from brain_games.engine import run_game
from brain_games.games.constants import GCD_INSTRUCTION


def get_nums_and_res_gcd():
    num1, num2 = random.randint(0, 100), random.randint(0, 100)
    nums = f'{num1} {num2}'
    return nums, str(math.gcd(num1, num2))


def run_gcd_game():
    run_game(get_nums_and_res_gcd, GCD_INSTRUCTION)
