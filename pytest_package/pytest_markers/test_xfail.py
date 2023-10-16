import pytest

username = "admin123"

# @pytest.mark.xfail
def test_validate():
	assert username == "admin", "usernames are not equal"
	print(username)

	# if username != "admin":
	# 	raise ValueError
	# else:
	# 	print(username)

#####################################################################
import pytest


class TestCalculator:
	a = 10
	b = 0

	def test_add(self):
		print( 2 + 3)

	@pytest.mark.xfail
	def test_div(self):
		print(self.a / self.b)