from number_guess_scenario import NumberGuessScenario
from number_comparer_factory import NumberComparerFactory
from user_interface import UserInterface

def create_number_guess_scenario(min_number: int, max_number: int):
    return NumberGuessScenario(NumberComparerFactory(min_number, max_number), UserInterface())

number_scenario = create_number_guess_scenario(1, 100)
number_scenario.start()