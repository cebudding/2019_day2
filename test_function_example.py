import numpy as np
import pytest

from maxima import find_maxima

test_cases = [
([0,1,2,1,2,1,0],[2,4]),
([4,2,1,3,1,2],[0,3,5]),
([4,2,1,3,1,5],[0,3,5]),
([1, 2, 2, 1],[1,2]),
([1, 2, 2, 3, 1],[3]),
([3, 2, 2, 3],[0,3]),
([1, 3, 2, 2, 1],[1])
]

@pytest.mark.parametrize('inp, exp', test_cases)
def test_maxima(inp, exp):
    out = find_maxima(inp)
    assert out == exp
