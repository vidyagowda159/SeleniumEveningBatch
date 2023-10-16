import pytest

# parameterize("arg_names",[(arg_values)])

@pytest.mark.parametrize("a, b", [(1, 2), (4, 7)])
def test_add(a, b):
	assert a + b == 2, "Sum is not equal to 2"


