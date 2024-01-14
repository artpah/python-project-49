from random import randint


from brain_games.engine import run_game


def get_num_and_res():
    num = randint(0, 100)

    def res():
        if num < 2:
            return 'no'
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return 'no'
        return 'yes'
    return num, res()


def run_prime_game():
    PRIME_INS = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(get_num_and_res, PRIME_INS)
