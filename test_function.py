import numpy as np
from maxima import find_maxima

def test_1():
    assert find_maxima([0, 1, 2, 1, 2, 1, 0]) == [2,4]

def test_2():
    x = [-i**2 for i in range(-3, 4)]
    assert find_maxima(x) == [3]

def test_3():
    x = [np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)]
    assert find_maxima(x)
