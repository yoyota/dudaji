import unittest
from queue_prac0 import LinkedListQueue

data_structure = LinkedListQueue()


class Test_01(unittest.TestCase):
    def test(self):
        result = data_structure.is_empty()
        self.assertEqual(result, True, msg="is_empty test fail")


class Test_02(unittest.TestCase):
    def test(self):
        with self.assertRaises(IndexError):
            data_structure.dequeue()


class Test_03(unittest.TestCase):
    def test(self):
        for i in range(100):
            data_structure.enqueue(i)
        result = len(data_structure)
        self.assertEqual(result, 100, msg="lenth is diffrent")


class Test_04(unittest.TestCase):
    def test(self):
        for i in range(100):
            result = data_structure.dequeue()
            length = len(data_structure)
            self.assertEqual(length, 99 - i, msg="length is diffrent")
            self.assertEqual(result, i, msg="return value fail")


if __name__ == '__main__':
    unittest.main()
