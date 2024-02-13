import random
from brain_games.engine import run_game
from brain_games.constants import PRIME_INSTRUCTION


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_num_and_prime_ans():
    num = random.randint(0, 100)
    prime_ans = 'yes' if is_prime(num) else 'no'
    return num, prime_ans


def run_prime_game():
    run_game(get_num_and_prime_ans, PRIME_INSTRUCTION)
