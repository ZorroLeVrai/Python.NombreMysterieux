from number_comparer_factory import NumberComparerFactory
from compare_result import CompareResult
from user_interface import UserInterface

class NumberGuessScenario:
    def __init__(self, number_comparer_factory: NumberComparerFactory, user_interface: UserInterface):
        self.number_comparer = number_comparer_factory.create()
        self.min_number = number_comparer_factory.min_number
        self.max_number = number_comparer_factory.max_number
        self.ui = user_interface
        self.nb_guess = 0
        self.number_found = False

    def __check_number(self, num: int) -> CompareResult:
        comparer_result = self.number_comparer.evaluate(num)
        self.number_found = (comparer_result == CompareResult.EQUAL)
        return comparer_result

    def __get_number(self):
        self.nb_guess += 1
        return self.ui.input_number(self.min_number, self.max_number)
    
    def guess_work(self):
        number_guessed = self.__get_number()
        comparison_result = self.__check_number(number_guessed)
        self.ui.output_hint(comparison_result)

    def start(self):
        while not self.number_found:
            self.guess_work()

        self.ui.output_result(self.nb_guess)