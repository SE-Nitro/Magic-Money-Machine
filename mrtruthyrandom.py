import random


def public_number(round_num, rounds_won):
    val = random.randint(0, 20)
    distribute = val
    return val, distribute


def real_number(round_num, rounds_won, others_tickets, distribute):
    return (distribute + 5) % 21
