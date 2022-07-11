import random

def number():
    return random.randint(11, 15)

def test_number():
    no = number()
    assert 0 <= no <= 10 

# https://realpython.com/pytest-python-testing/ 
# https://towardsdatascience.com/github-automated-testing-python-fdfe5aec9446

