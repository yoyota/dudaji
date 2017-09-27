class AbstracStack:
    def __init__(self):
        self.top = 0

    def __len__(self):
        return self.top

    def is_empty(self):
        return self.top == 0

class ArrayStack(AbstracStack):
    def __init__(self, size = 10):
        AbstracStack.__init__(self)
        self.arr = [None] * size

    def expand(self):
        new_arr = [None] * len(self.arr) * 2
        for i, element in enumerate(self.arr):
            new_arr[i] = element
        self.arr = new_arr

    def push(self, value):
        if len(self.arr) == self.top:
            self.expand()
        self.arr[self.top] = value
        self.top += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        value = self.arr[self.top - 1]
        self.top -= 1
        return value


