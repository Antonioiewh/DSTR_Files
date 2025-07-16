class pancake:
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

    def peek(self):
        if self.is_empty():
            print("Top requested on empty stack!")
            raise IndexError("top from empty stack")
        print(f"Top is {self._data[-1]}")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)
    
#Testcases
#teststack = pancake()
#while True:
    #inputnum = input("Enter a number to push onto the stack (or 'E' to stop): ")
    #if inputnum == 'E':
        #print("Exiting input loop.")
        #break
    #if not inputnum:
        #break
    #teststack.push(int(inputnum))


#for i in teststack._data:
    #print(f"Current stack item: {i}")