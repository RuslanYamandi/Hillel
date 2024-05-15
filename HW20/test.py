
import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_fibonacci(self):
        correct_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
        fib = utils.Fibonacci()
        for index in range(len(correct_sequence)):
            response = fib(index)
            self.assertEqual(response, correct_sequence[index], 'Fibonacci test failed.')

    def test_formatted_name(self):
        case = utils.formatted_name('John', 'Doe', '')
        self.assertEqual(case, 'John Doe')
        case = utils.formatted_name('John', 'Doe', 'van')
        self.assertEqual(case, 'John Van Doe')


if __name__ == '__main__':
    unittest.main()
