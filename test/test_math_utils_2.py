import pytest
import code.math_utils as cma


@pytest.mark.parametrize("a,b,expected",[
    (1,2,3),
    (-1,1,0),
    (0,0,0),
    (1.5,2.5,4.0),
    (-1.0,1.0,0.0)
])
def test_add(a,b,expected):
    assert cma.add(a,b) == expected