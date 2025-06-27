# -------------------------------
# Question 4: Linked List with Head and Tail References
# -------------------------------

# Singly linked list class with both head and tail references
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # a. Append a node to the list using head and tail references
    # - If the list is empty, set both head and tail to the new node.
    # - Otherwise, set tail.next to the new node and update tail.
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # b. Remove a target node from the list using head and tail references
    # - If the list is empty, do nothing.
    # - If the node to remove is the head, update head (and tail if needed).
    # - Otherwise, traverse to find the node, update links, and update tail if needed.
    def remove(self, target):
        if self.head is None:
            return
        # If target is head
        if self.head == target:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return
        # Find the node before target
        prev = self.head
        while prev.next and prev.next != target:
            prev = prev.next
        if prev.next == target:
            prev.next = target.next
            # If target is tail, update tail
            if target == self.tail:
                self.tail = prev

# -------------------------------
# Example Usage for Question 4
# -------------------------------

# Create a linked list and append nodes
ll = LinkedList()
ll.append(28)
ll.append(19)
ll.append(45)
ll.append(13)
ll.append(7)

# Print list
print("Initial list:", end=" ")
current = ll.head
while current:
    print(current.data, end=" ")
    current = current.next
print("\nHead:", ll.head.data if ll.head else None, "Tail:", ll.tail.data if ll.tail else None)

# Remove a node (e.g., node with value 45)
# First, find the node with value 45
current = ll.head
while current and current.data != 45:
    current = current.next
if current:
    ll.remove(current)

# Print list after removal
print("After removing 45:", end=" ")
current = ll.head
while current:
    print(current.data, end=" ")
    current = current.next
print("\nHead:", ll.head.data if ll.head else None, "Tail:", ll.tail.data if ll.tail else None)

# Remove tail node (node with value 7)
current = ll.head
while current and current.data != 7:
    current = current.next
if current:
    ll.remove(current)

# Print list after removing tail
print("After removing tail (7):", end=" ")
current = ll.head
while current:
    print(current.data, end=" ")
    current = current.next
print("\nHead:", ll.head.data if ll.head else None, "Tail:", ll.tail.data if ll.tail else None)

# Remove all nodes
while ll.head:
    ll.remove(ll.head)

print("After removing all nodes:")
print("Head:", ll.head, "Tail:", ll.tail)

# -------------------------------
# Explanation:
# - The LinkedList class maintains both head and tail references.
# - append(data): Adds a new node at the end in O(1) time using the tail reference.
# - remove(target): Removes a given node, updating head and tail as needed.
# - Example usage shows appending, removing a middle node, removing the tail, and clearing the list.
# -------------------------------