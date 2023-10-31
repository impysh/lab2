import bmi
def test_underweight():
    result = bmi.calculate_bmi(height=1.73, weight=57)
    assert result == -1

def test_normal_weight():
    result = bmi.calculate_bmi(height=1.73, weight=70)
    assert result == 0

def test_overweight():
    result = bmi.calculate_bmi(height=1.73, weight=90)
    assert result == 1