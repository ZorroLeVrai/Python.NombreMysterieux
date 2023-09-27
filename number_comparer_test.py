import unittest
from number_comparer import NumberComparer
from compare_result import CompareResult

class GuessNumberTest(unittest.TestCase):

    def test_compare_values(self):
        #Arrange
        num_comparer = NumberComparer(10)

        #Act & Assert
        self.assertEqual(num_comparer.evaluate(9), CompareResult.MORE)
        self.assertEqual(num_comparer.evaluate(0), CompareResult.MORE)
        self.assertEqual(num_comparer.evaluate(11), CompareResult.LESS)
        self.assertEqual(num_comparer.evaluate(10), CompareResult.EQUAL)

if __name__ == "__main__":
    unittest.main()