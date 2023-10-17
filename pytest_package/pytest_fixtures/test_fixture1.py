import pytest

@pytest.fixture()
def greet():
	print("Helloo")

def test_func(greet):
	print("in test function")

def test_spam(greet):
	print("in test spam")

