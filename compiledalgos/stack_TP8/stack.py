class Stack:
    """A simple stack implementation using a Python list."""

    def __init__(self):
        self._data = []
        print("Initialized empty stack.")

    def push(self, item):
        self._data.append(item)
        print(f"Pushed {item}: {self._data}")

    def pop(self):
        if self.is_empty():
            print("Pop attempted on empty stack!")
            raise IndexError("pop from empty stack")
        item = self._data.pop()
        print(f"Popped {item}: {self._data}")
        return item

    def top(self):
        if self.is_empty():
            print("Top requested on empty stack!")
            raise IndexError("top from empty stack")
        print(f"Top is {self._data[-1]}")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

# Test cases with stack traces
if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.top()
    s.pop()
    s.top()
    s.pop()
    s.pop()
    try:
        s.pop()
    except IndexError:
        print("Caught exception on pop from empty stack.")
    print("Final stack (should be empty):", s._data)