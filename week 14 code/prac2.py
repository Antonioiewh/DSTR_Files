class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    # Creates qn empty queue
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = 0
    
    # Impplementation of Queue ADT using a linked list
    def isEmpty(self):
        return self._qhead is None 
    
    def __len__(self):
        return self._count
    
    def enqueue(self, item):
        node = QueueNode(item)
        if self.isEmpty():
            self._qhead = node
            self._qtail = node
        else:
            self._qtail.next = node
        self._qtail = node
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        item = self._qhead.data
        self._qhead = self._qhead.next
        if self._qhead is None:
            self._qtail = None
        self._count -= 1
        return item
    



# Test cases for Queue implementation
if __name__ == '__main__':
    print("=== Queue Test Cases ===\n")
    
    # Test 1: Create empty queue and check initial state
    print("Test 1: Empty Queue")
    q = Queue()
    print(f"Is empty: {q.isEmpty()}")
    print(f"Length: {len(q)}")
    print()
    
    # Test 2: Enqueue single item
    print("Test 2: Enqueue Single Item")
    q.enqueue(10)
    print(f"After enqueue(10):")
    print(f"Is empty: {q.isEmpty()}")
    print(f"Length: {len(q)}")
    print()
    
    # Test 3: Enqueue multiple items
    print("Test 3: Enqueue Multiple Items")
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    print(f"After enqueue(20, 30, 40):")
    print(f"Length: {len(q)}")
    print()
    
    # Test 4: Dequeue items (FIFO order)
    print("Test 4: Dequeue Items (FIFO)")
    item1 = q.dequeue()
    print(f"Dequeued: {item1}")
    print(f"Length after dequeue: {len(q)}")
    
    item2 = q.dequeue()
    print(f"Dequeued: {item2}")
    print(f"Length after dequeue: {len(q)}")
    print()
    
    # Test 5: Mix enqueue and dequeue operations
    print("Test 5: Mix Operations")
    q.enqueue(50)
    print(f"After enqueue(50), Length: {len(q)}")
    
    item3 = q.dequeue()
    print(f"Dequeued: {item3}")
    print(f"Length: {len(q)}")
    print()
    
    # Test 6: Dequeue until empty
    print("Test 6: Dequeue Until Empty")
    while not q.isEmpty():
        item = q.dequeue()
        print(f"Dequeued: {item}, Length: {len(q)}")
    
    print(f"Final state - Is empty: {q.isEmpty()}")
    print()
    
    # Test 7: Enqueue after emptying
    print("Test 7: Enqueue After Emptying")
    q.enqueue(100)
    q.enqueue(200)
    print(f"After enqueue(100, 200):")
    print(f"Length: {len(q)}")
    print(f"Is empty: {q.isEmpty()}")
    print()
    
    # Test 8: Error handling - dequeue from empty queue
    print("Test 8: Error Handling")
    q.dequeue()  # Remove 100
    q.dequeue()  # Remove 200
    try:
        q.dequeue()  # This should raise an assertion error
    except AssertionError as e:
        print(f"Caught expected error: {e}")
    print()
    
    # Test 9: Comprehensive test with large dataset
    print("Test 9: Large Dataset Test")
    large_q = Queue()
    
    # Enqueue numbers 1-10
    for i in range(1, 11):
        large_q.enqueue(i)
    print(f"Enqueued 1-10, Length: {len(large_q)}")
    
    # Dequeue first 5
    dequeued_items = []
    for _ in range(5):
        dequeued_items.append(large_q.dequeue())
    print(f"Dequeued first 5: {dequeued_items}")
    print(f"Remaining length: {len(large_q)}")
    
    # Enqueue more items
    for i in range(11, 16):
        large_q.enqueue(i)
    print(f"Enqueued 11-15, Final length: {len(large_q)}")
    
    # Dequeue all remaining
    remaining = []
    while not large_q.isEmpty():
        remaining.append(large_q.dequeue())
    print(f"All remaining items: {remaining}")
    print(f"Final empty state: {large_q.isEmpty()}")