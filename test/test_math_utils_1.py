import pytest
from code.math_utils import add

def test_add_integers():
    assert add(1,2) == 3
    assert add(-1,1) == 0
    assert add(0,0) == 0

def test_add_foloats():
    assert add(1.5,1.5) == 3
    assert add(-1.1,1.1) == 0.0

def test_add_with_zero():
    assert add(0,5) == 5
    assert add(0,-5) == -5