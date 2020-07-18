import unittest


def fizzbuzz(number):
    return 'Fizz'


class TestFizzBuzz(unittest.TestCase):
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')


unittest.main()