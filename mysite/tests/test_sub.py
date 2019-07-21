import unittest


def sub(a, b):
	return a - b


# 必须继承 unittest.TestCase
class TestSub(unittest.TestCase):

	def setUp(self):
		print("测试用例开始之前执行")

	def tearDown(self):
		print("用例结束的时候执行")

	# 必须以“test”开头
	def test_sub1(self):
		a = sub(5, 3)
		print("test_sub")
		self.assertEqual(a, 2)

	def test_sub2(self):
		a = sub(5.5, 3.1)
		print("test_sub2")
		self.assertEqual(a, 2.4)


if __name__ == "__main__":
	unittest.main()