def merge_sort(case):
    n = len(case)

    if n < 2:
        return case

    middle = n // 2
    left = case[:middle]
    right = case[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while len(left) != 0:
        result.append(left.pop(0))
    while len(right) != 0:
        result.append(right.pop(0))

    return result
