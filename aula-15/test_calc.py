import math

def calculate_hypotenuse(a, b):
    hypo = math.sqrt(a**2 + b**2)
    return hypo

def test_hypotenuse1():
    side_a = 3
    side_b = 4
    expected_hypo = 6
    calculated_hypo = calculate_hypotenuse(side_a, side_b)
    assert calculated_hypo == expected_hypo

def test_hypotenuse2():
    side_a = 3
    side_b = 4
    expected_hypo = 6
    calculated_hypo = calculate_hypotenuse(side_a, side_b)
    assert calculated_hypo == expected_hypo