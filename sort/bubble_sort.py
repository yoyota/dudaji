def bubble_sort(test_case):
    n = len(test_case)

    while n != 0:
        new_n = 0

        for i in range(1, n):
            if test_case[i - 1] > test_case[i]:
                test_case[i - 1], test_case[i] = test_case[i], test_case[i - 1]
                new_n = i
        n = new_n

    return test_case
