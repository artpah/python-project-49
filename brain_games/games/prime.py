import random
from brain_games.engine import run_game
from brain_games.games.constants import PRIME_INSTRUCTION


def get_num_and_prime_ans():
    num = random.randint(0, 100)

    def is_prime():
        return 'yes' if num >= 2 \
               and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) \
               else 'no'
    return num, is_prime()


def run_prime_game():
    run_game(get_num_and_prime_ans, PRIME_INSTRUCTION)
