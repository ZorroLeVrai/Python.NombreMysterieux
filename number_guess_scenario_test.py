import unittest
from number_guess_scenario import NumberGuessScenario
from mocks import NumberComparerFactoryMock, UserInterfaceMock

class GuessNumberTest(unittest.TestCase):

    def test_compare_values(self):
        def check_step(user_input: int, expected_nb_guess: int, expected_number_found: bool):
            user_interface_mock.user_input = user_input
            guess_scenario.guess_work()
            self.assertEqual(guess_scenario.nb_guess, expected_nb_guess)
            self.assertEqual(guess_scenario.number_found, expected_number_found)

        #Arrange
        number_factory_mock = NumberComparerFactoryMock(10)
        user_interface_mock = UserInterfaceMock()
        guess_scenario = NumberGuessScenario(number_factory_mock, user_interface_mock)

        #Act & Assert
        check_step(0, 1, False);
        check_step(9, 2, False);
        check_step(11, 3, False);
        check_step(10, 4, True);


if __name__ == "__main__":
    unittest.main()