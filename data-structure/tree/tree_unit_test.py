import unittest
from tree import Tree


class TreeTest(unittest.TestCase):

    def test_create(self):
        my_tree = Tree()
        self.assertEqual(None, my_tree.root)

    def test_insert(self):
        my_tree = Tree()
        my_tree.insert(0)
        self.assertEqual(str(my_tree), '0, None, None')

        my_tree.insert(1)
        self.assertEqual(str(my_tree), '0, None, 1, None, None')

        my_tree.insert(-1)
        self.assertEqual(str(my_tree), '0, -1, None, None, 1, None, None')

    def test_search(self):
        my_tree = Tree()
        my_tree.insert(0)
        my_tree.insert(-1)
        my_tree.insert(1)

        self.assertEqual(1, my_tree.search(1))

    def test_remove(self):
        my_tree = Tree()
        my_tree.insert(0)
        my_tree.insert(-1)
        my_tree.insert(1)
        my_tree.remove(0)

        self.assertEqual(str(my_tree), '1, -1, None, None, None')


if __name__ == '__main__':
    unittest.main()