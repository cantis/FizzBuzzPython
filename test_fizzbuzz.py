import pytest
from app import main

def test_normal():
    result = main()
    assert result[1] == '2'

def test_fizz_on_three():
    result = main()
    assert result[2] == 'Fizz'

def test_buzz_on_five():
    result = main()
    assert result[4] == 'Buzz'

def test_fizbuzz_on_threefive():
    result = main()
    assert result[14] == 'FizzBuzz'
