from number_comparer import NumberComparer
from compare_result import CompareResult

class NumberComparerFactoryMock:
    min_number = 0
    max_number = 0

    def __init__(self, my_number: int):
        self.my_number = my_number

    def create(self):
        return NumberComparer(self.my_number)
    
class UserInterfaceMock:
    def __init__(self):
        self.user_input = 0

    def input_number(self, min_number: int, max_number: int) -> int:
        return self.user_input

    def output_hint(self, position_hint: CompareResult) -> None:
        pass

    def output_result(self, nb_guess: int) -> None:
        pass
