from number_comparer import NumberComparer
from random import randint

class NumberComparerFactory:
    def __init__(self, min_number: int, max_number: int):
        self.min_number = min_number
        self.max_number = max_number

    def create(self):
        return NumberComparer(randint(self.min_number, self.max_number))