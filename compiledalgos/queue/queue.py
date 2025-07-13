class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        assert not self.is_empty(), "Dequeue from empty queue"
        return self.items.pop(0)

    def peek(self):
        assert not self.is_empty(), "Peek from empty queue"
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)