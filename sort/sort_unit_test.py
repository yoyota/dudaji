import unittest
import datetime
import random
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from heap_sort import heap_sort


def time_check(fn, case):
    start_time = datetime.datetime.now()

    if isinstance(fn, str):
        result = sorted(case)
    else:
        result = fn(case)
        fn = str(fn)
        fn = fn.split(' ')[1]

    end_time = datetime.datetime.now()
    print(fn, 'time =', end_time - start_time)

    return result


test_count = 12
test_case_scope = [1, 100]
test_case = []

for i in range(test_count):
    test_case.append(random.randint(test_case_scope[0], test_case_scope[1]))

python_sroted = time_check('python sorted', test_case)


class SortAlgorithmTest(unittest.TestCase):
    def test_bubble_sort(self):
        case = test_case[:]
        result = time_check(bubble_sort, case)
        self.assertEqual(python_sroted, result)

    def test_merge_sort(self):
        case = test_case[:]
        result = time_check(merge_sort, case)
        self.assertEqual(python_sroted, result)

    def test_heap_sort(self):
        case = test_case[:]
        result = time_check(heap_sort, case)
        self.assertEqual(python_sroted, result)


if __name__ == '__main__':
    unittest.main()
