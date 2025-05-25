import pytest

class TestCalculator:

    def test_add(self, calc):
        assert calc.add(3,5) == 8

    def test_subtract(self, calc):
        assert calc.subtract(10, 4) == 6

    def test_multiply(self, calc):
        assert calc.multiply(2,3) == 6

    def test_divide(self, calc):
        assert calc.divide(10, 2) == 5

    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(5, 0)