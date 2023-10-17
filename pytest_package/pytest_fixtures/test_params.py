import pytest


@pytest.fixture(params=[10, 20, 30])
def fixture(request):
	value = request.param
	print("Before.....")
	yield value
	print("After......")


# @pytest.mark.parametrize("a", [1, 2, 3, 4, 5])
# def test_add(a, fixture):
# 	assert a + 5 == 10, "Not equal to 10"


def test_display(fixture):
	x = fixture
	print("in test display", x)