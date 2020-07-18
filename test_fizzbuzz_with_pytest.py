def fizzbuzz(number):
    if number == 5:
        return 'Buzz'


def test_input_5_should_get_buzz():
    result = fizzbuzz(5)
    assert result == 'Buzz'
