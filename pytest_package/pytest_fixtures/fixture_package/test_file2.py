import pytest

class TestCalculator:
	a = 10
	b = 9

	@pytest.mark.group1
	def test_add(self):
		print(2 + 3)

	@pytest.mark.group2
	def test_sub(self):
		print(1 - 5)

	def test_mul(self):
		print(1 * 4)

	@pytest.mark.group1
	def test_div(self):
		print(self.a / self.b)


# pytest test_file2.py -vs
# batch execution: pytest -vs
# parallel execution: pip install pytest-xdist
#   pytest -vs -n 2