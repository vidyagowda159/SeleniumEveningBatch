import pytest

@pytest.fixture(scope="class")
def greet():
	print("Helloo")         # setup
	yield
	print("end...../")      # teardown


@pytest.mark.usefixtures("greet")
class TestSample:

	def test_fun1(self):
		print("in function 1")

	def test_fun2(self):
		print("in function 2")
