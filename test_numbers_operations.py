import unittest
import numbers_operations


class TestNumbers(unittest.TestCase):

    def test_numbers_positive(self):
        result = numbers_operations.add_two_numbers(4, 6)
        expected = 10
        self.assertEqual(result, expected)

    def test_one_number_negative(self):
        result = numbers_operations.add_two_numbers(4, -6)
        expected = -2
        self.assertEqual(result, expected)

    def test_one_number_invalid(self):
        with self.assertRaises(TypeError):
            numbers_operations.add_two_numbers(5, "hi")

    def test_divide_by_number(self):
        result = numbers_operations.divide_two_numbers(7, 2)
        expected = 3.5
        self.assertEqual(result, expected)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            numbers_operations.divide_two_numbers(6, 0)


if __name__ == "__main__":
    unittest.main()