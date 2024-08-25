#Tests
import pytest
from myfile import fibonacci

def test_correct():
  assert fibonacci(5) == 8
