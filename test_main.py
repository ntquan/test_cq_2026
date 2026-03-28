import unittest
from main import calculate_sub_function, calculate_sum_and_average, get_numbers_from_user

class TestCalculateFunctions(unittest.TestCase):

    def test_valid_numbers(self):
        self.assertEqual(calculate_sum_and_average([1, 2, 3]), (6, 2.0))

    def test_empty_list(self):
        with self.assertRaises(ValueError) as context:
            calculate_sum_and_average([])
        self.assertEqual(str(context.exception), "Dãy số không được rỗng nha.")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average([1, -2, 3])

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            calculate_sum_and_average(["a", "b", "c"])

    # write test calculate_sub_function
    def test_calculate_sub_function_valid(self):
        self.assertEqual(calculate_sub_function(5, 3), 1)

    def test_calculate_sub_function_negative(self):
        with self.assertRaises(ValueError):
            calculate_sub_function(-5, 3)


if __name__ == '__main__':
    unittest.main()
