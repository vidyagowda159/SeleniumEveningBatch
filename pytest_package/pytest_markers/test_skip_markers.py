import pytest


class TestCalculator:
	a = 10
	b = 9

	def test_add(self):
		print( 2 + 3)

	@pytest.mark.skip("Skipping subtraction test case")
	def test_sub(self):
		print(1 - 5)

	def test_mul(self):
		print(1 * 4)

	@pytest.mark.skipif(b == 0, reason="denominator is zero")
	def test_div(self):
		print(self.a / self.b)
