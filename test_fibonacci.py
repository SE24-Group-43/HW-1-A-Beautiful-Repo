#Tests
import pytest
from myfile import fibonacci

def test_fibonacci_0():
  assert fibonacci(5) == 5

# def test_incorrect_fibonnaci():
#   with pytest.raises(ValueError):
#     fibonacci(-1) 
