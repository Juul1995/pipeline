import random

def number():
    return random.randint(0, 10)

def test_number():
    no = number()
    assert 0 <= no <= 10 

# https://realpython.com/pytest-python-testing/ 