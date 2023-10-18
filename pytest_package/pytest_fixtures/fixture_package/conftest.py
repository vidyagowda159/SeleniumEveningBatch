# sharing the fixtures among all the testcases in the
# same package

import pytest

@pytest.fixture(autouse=True, scope="session")  # scope="module"
def greet():
	print("hellooooo")
	yield
	print("end....")
