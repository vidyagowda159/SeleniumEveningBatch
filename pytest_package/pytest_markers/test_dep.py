# pip install pytest-dependency
import pytest

@pytest.mark.dependency(name="add")
def test_add():
	assert True

@pytest.mark.dependency(depends=["add"])
def test_sub():
	print("in sub")
	assert True

