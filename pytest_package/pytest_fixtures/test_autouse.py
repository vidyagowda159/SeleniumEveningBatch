import pytest

@pytest.fixture(autouse=True)
def greet():
	print("Helloo")

def test_func():
	print("in test function")

def test_spam():
	print("in test spam")