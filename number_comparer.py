from compare_result import CompareResult

class NumberComparer:
    def __init__(self, number: int):
        self.number = number

    def evaluate(self, number_guess: int) -> CompareResult:
        if (self.number < number_guess):
            return CompareResult.LESS
        
        if (self.number > number_guess):
            return CompareResult.MORE
        
        return CompareResult.EQUAL
