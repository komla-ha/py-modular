#myrandom.py


import importlib

random = importlib.import_module('random')

def gen_random_1p():
    return random.randint(0,9)


def gen_random_2p():
    return random.randint(10, 99)

