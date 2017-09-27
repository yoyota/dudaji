from heapq import heapify, heappop


def heap_sort(case):
    n = len(case)
    heapify(case)
    result = []
    for _ in range(n):
        result.append(heappop(case))
    return result
