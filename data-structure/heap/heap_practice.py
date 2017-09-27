class Heap:
    def __init__(self, comparator):
        self.heap = []
        self.comparator = comparator

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)

    def left_index(self, index):
        return index * 2 + 1

    def right_index(self, index):
        return index * 2 + 2

    def parent_index(self, index):
        return (index - 1) // 2

    def sift_up(self, index):
        while index > 0:
            parent = self.parent_index(index)

            if self.comparator(self.heap[parent], self.heap[index]):
                return
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent

    def push(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)

    def sift_down(self, index):
        while True:
            left = self.left_index(index)
            right = self.right_index(index)
            next = index

            if left < len(self.heap) and self.comparator(self.heap[left], self.heap[next]):
                next = left

            if right < len(self.heap) and \
                    self.comparator(self.heap[right], self.heap[next]):
                next = right

            if index == next:
                return

            self.heap[next], self.heap[index] = self.heap[index], self.heap[next]
            index = next

    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("empty")

        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)

        return value
