class AbstractQueue:
    def __init__(self):
        self.top = 0

    def __len__(self):
        return self.top

    def is_empty(self):
        return self.top == 0


class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue(AbstractQueue):
    def __init__(self):
        AbstractQueue.__init__(self)
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = QueueNode(value)

        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.top += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.front.value

        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        self.top -= 1
        return value
