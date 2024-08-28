#Tests
import pytest
from myfile import fibonacci

def test_fibonacci():
  assert fibonacci(5) == 5

def test_fibonacci1():
  assert fibonacci(-1) == 0

#Testing

# def test_incorrect_fibonnaci():
#   with pytest.raises(ValueError):
#     fibonacci(-1) 
