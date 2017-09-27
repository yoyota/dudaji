import unittest
from stack_prac3 import ArrayStack
# from stack_prack3 import LinkedListStack

my_stack = ArrayStack();

#is_empty test
class Test_01(unittest.TestCase):
    def test(self):
        result = my_stack.is_empty()
        self.assertEqual(result, True, msg = "is_empty test fail")

#empty stack pop method error check
class Test_02(unittest.TestCase):
    def test(self):
        with self.assertRaises(IndexError):
            my_stack.pop()

#method push, expand and len test
class Test_03(unittest.TestCase):
    def test(self):
        for i in range(100):
            my_stack.push(i)
        result = len(my_stack)
        self.assertEqual(result, 100, msg = "lenth is diffrent")

#method pop check
class Test_04(unittest.TestCase):
    def test(self):
        result = my_stack.pop()
        self.assertEqual(result, 99, msg = "pop return value fail")
        result = len(my_stack)
        self.assertEqual(result, 99, msg = "pop remove fail")

if __name__ == '__main__':
    unittest.main()
