import unittest

def add(a, b):
    return a + b

def sub(a, b):
	return a - b

# 必须继承 unittest.TestCase
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
	#unittest.main()
	# 测试套件
	suit = unittest.TestSuite()
	suit.addTest(TestSub("test_sub2"))
	suit.addTest(TestAdd("test_add3"))

	# 测试运行
	runner = unittest.TextTestRunner()
	runner.run(suit)


012347502139475lasdhjglqwsdjflaskwj

10w45oqwiejfroqisjeflqskjedflqekjtrf => helloword

base64 

2019-11-11 12:00:00  == "2019-11-11 12:00:00"


def jiami(a):
	加密的过程
	return 加密的结果


a = jiami("hello")
b = 加密的过程

a(加密的结果) == b
