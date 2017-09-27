import unittest
from hprac6 import HashTable


class HashFunctionTest(unittest.TestCase):

    def test(self):
        my_hash = HashTable(10)
        hash10 = my_hash.hash_fn

        self.assertIn(hash10("a"), range(10))
        self.assertIn(hash10("b"), range(10))
        self.assertIn(hash10("ab"), range(10))
        self.assertIn(hash10("more than a feeling"), range(10))


class HashTableTest(unittest.TestCase):
    def test_create(self):
        ht = HashTable(10)
        self.assertRaises(KeyError, ht.set, 1, 2)
        self.assertEqual(ht.capacity, 10)
        self.assertEqual(ht.size, 0)

        ht = HashTable()
        self.assertEqual(ht.capacity, 256)

    def test_set_and_get(self):
        ht = HashTable(10)
        ht.set('a', 1)
        self.assertEqual(ht.get('a'), 1)
        self.assertEqual(ht.size, 1)

        # Check update functionality
        ht.set('a', 2)
        self.assertEqual(ht.get('a'), 2)
        self.assertEqual(ht.size, 1)

        # Make sure we can add a 2nd element
        ht.set('b', 10)
        self.assertEqual(ht.get('b'), 10)
        self.assertEqual(ht.get('a'), 2)
        self.assertEqual(ht.size, 2)

    def test_bad_get(self):
        ht = HashTable(10)
        self.assertRaises(KeyError, ht.get, 'a')

    def test_remove(self):
        ht = HashTable(10)
        self.assertRaises(KeyError, ht.remove, 'a')

        ht.set('a', 1)
        removed_item = ht.remove('a')
        self.assertEqual(removed_item, 1)
        self.assertEqual(ht.size, 0)


if __name__ == '__main__':
    unittest.main()
