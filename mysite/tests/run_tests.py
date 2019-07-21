import unittest
import os
test_dir = os.path.dirname(os.path.abspath(__file__))
print(test_dir)

suit = unittest.defaultTestLoader.discover(test_dir, "test_*.py")

runner = unittest.TextTestRunner()
runner.run(suit)
