from math_utils import add
import pytest

@pytest.mark.parametrize("a,b,expected",[
    (1,2,3),
    (-1,1,0),
    (0,0,0),
    (1.5,2.5,4.0),
    (-1.0,1.0,0.0)
])
def test_add(a,b,expected):
    assert add(a,b) == expected