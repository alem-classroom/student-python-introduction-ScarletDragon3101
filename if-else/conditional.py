import random

def is_positive(num):
    if num > 0:
        return True
    else: return False
    # return true if num is positive, otherwise return false

def is_even(num):
    if num % 2:
        return True
    else: return False
    # return true if num is even, otherwise return false


def is_positive_and_even(num):
    if num % 2 and num > 0:
        return True
    else: return False
    # return true if num is positive and even, otherwise return false


def is_positive_or_even(num):
    if num % 2 or num > 0:
        return True
    else: return False
    # return true if num is positive or even, otherwise return false

