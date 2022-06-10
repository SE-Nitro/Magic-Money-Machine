import random


def main(round_num, others_money):
    if round_num == 1:
        money_insert = random.randint(0, 100)
    else:
        money_insert = (
            random.choice(others_money[-1]) if others_money else random.randint(0, 100)
        )
    return money_insert
