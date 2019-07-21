import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):

	def setUp(self):
		print("测试用例开始之前执行")

	def tearDown(self):
		print("用例结束的时候执行")

	# 必须以“test”开头
	def test_add1(self):
		a = add(3, 5)
		print("test_add1")
		self.assertEqual(a, 8)

	def test_add2(self):
		a = add(3.2, 5.5)
		print("test_add2")
		self.assertEqual(a, 8.7)

	def test_add3(self):
		a = add(-3.2, 5.5)
		print("test_add3")
		self.assertEqual(a, 2.3)

	def test_add4(self):
		a = add("hello", "world")
		print("test_add4")
		self.assertEqual(a, "helloworld")

if __name__ == "__main__":
	unittest.main()