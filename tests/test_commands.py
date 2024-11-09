from mike_example.commands import adder
import pytest

@pytest.mark.parametrize("x, y, expected", [(1,3,4), (0.1, 0.5, 0.6)])
def test_adder(x, y, expected):
    assert next(adder(x, y)) == expected