import math
import unittest
import datetime
from hash_table_practice import HashTable


def create_input(count, container):
    is_list = True if isinstance(container, list) else False

    for i in range(count):
        key = "qoontree" + str(i)
        if is_list:
            container.append(key)
        else:
            container.set(key, i)
    return container


def search_test(count, container):
    is_list = True if isinstance(container, list) else False

    for i in range(count):
        key = "qoontree" + str(i)

        if is_list:
            value = container.index(key)
        else:
            value = container.get(key)


class HashFunctionTest(unittest.TestCase):
    test_case_count = 10000

    def test_hash(self):
        before = datetime.datetime.now()

        my_hash = HashTable(math.floor(self.test_case_count * 1.2))
        my_hash = create_input(self.test_case_count, my_hash)
        search_test(self.test_case_count, my_hash)

        after = datetime.datetime.now()
        print('hash table =', after - before)

    def test_list(self):
        before = datetime.datetime.now()

        my_list = []
        my_list = create_input(self.test_case_count, my_list)
        search_test(self.test_case_count, my_list)

        after = datetime.datetime.now()
        print('list = ', after - before)


if __name__ == '__main__':
    unittest.main()
