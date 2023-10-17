import pytest

@pytest.fixture(autouse=True, scope="class")
def greet():
	print("Helloo")         # setup
	yield
	print("end...../")      # teardown


class TestSample:

	def test_fun1(self):
		print("in function 1")

	def test_fun2(self):
		print("in function 2")
