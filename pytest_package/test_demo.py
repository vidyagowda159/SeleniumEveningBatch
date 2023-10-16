def test_spam():
	print("in test spam")


class TestDemo:

	def test_func1(self):
		# print("in function 1")
		print(2 / 0)

	def test_func2(self):
		print("in function 2")

# pytest filename.py -vs
