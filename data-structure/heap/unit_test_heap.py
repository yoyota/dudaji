import unittest

from heap_practice import Heap


def max_heap(x, y):
    return x > y


def min_heap(x, y):
    return x < y


class HeapTest(unittest.TestCase):
    def test_max_heap(self):
        # Test push
        h = Heap(max_heap)

        h.push(5)
        self.assertEqual(str(h), "[5]")

        h.push(3)
        self.assertEqual(str(h), "[5, 3]")

        h.push(9)
        self.assertEqual(str(h), "[9, 3, 5]")

        h.push(1)
        self.assertEqual(str(h), "[9, 3, 5, 1]")

        h.push(20)
        self.assertEqual(str(h), "[20, 9, 5, 1, 3]")

        h.push(2)
        self.assertEqual(str(h), "[20, 9, 5, 1, 3, 2]")

        h.push(7)
        self.assertEqual(str(h), "[20, 9, 7, 1, 3, 2, 5]")

        h.push(21)
        self.assertEqual(str(h), "[21, 20, 7, 9, 3, 2, 5, 1]")

        # Test pop
        self.assertEqual(h.pop(), 21)
        self.assertEqual(h.pop(), 20)
        self.assertEqual(h.pop(), 9)
        self.assertEqual(h.pop(), 7)


    def test_min_heap(self):
        h = Heap(min_heap)

        h.push(5)
        self.assertEqual(str(h), "[5]")

        h.push(7)
        self.assertEqual(str(h), "[5, 7]")

        h.push(3)
        self.assertEqual(str(h), "[3, 7, 5]")

        h.push(4)
        self.assertEqual(str(h), "[3, 4, 5, 7]")

        h.push(-1)
        self.assertEqual(str(h), "[-1, 3, 5, 7, 4]")

        # Test pop
        self.assertEqual(h.pop(), -1)
        self.assertEqual(h.pop(), 3)
        self.assertEqual(h.pop(), 4)
        self.assertEqual(h.pop(), 5)
        h.push(-10)
        self.assertEqual(h.pop(), -10)
        self.assertEqual(h.pop(), 7)
        self.assertRaises(IndexError, h.pop)


if __name__ == '__main__':
    unittest.main()