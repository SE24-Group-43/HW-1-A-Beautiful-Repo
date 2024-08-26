#Tests
import pytest
from myfile import fibonacci

def test_fibonacci():
  assert fibonacci(5) == 5

def test_incorrect_fibonnaci():
    assert fibonacci(-1) is None 
