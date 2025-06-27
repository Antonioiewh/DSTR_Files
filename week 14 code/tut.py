# -------------------------------
# Node class definition for usage
# -------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# -------------------------------
# Question 1: Second-to-Last Node
# This function traverses the linked list to find and return the second-to-last node.
# - If the list has fewer than two nodes, it returns None.
# - It moves through the list until it finds the node whose next.next is None,
#   which is the node just before the last node.
# - Returns this second-to-last node.
# -------------------------------

def second_to_last(head):
    if head is None or head.next is None:
        return None
    current = head
    while current.next.next is not None:
        current = current.next
    return current

# -------------------------------
# Question 2: Concatenate Two Lists
# This function concatenates two singly linked lists L and M.
# - If L is empty, it returns M.
# - Otherwise, it traverses L to find its last node.
# - Sets the next of the last node of L to point to the head of M,
#   effectively joining the two lists.
# - Returns the head of the combined list.
# -------------------------------

def concatenate(L, M):
    if L is None:
        return M
    current = L
    while current.next is not None:
        current = current.next
    current.next = M
    return L

# -------------------------------
# Question 3: Recursive Node Count
# This function counts the number of nodes in a linked list using recursion.
# - If the current node is None, it returns 0 (base case).
# - Otherwise, it returns 1 plus the count of the rest of the list (recursive case).
# - Continues until the end of the list is reached.
# -------------------------------

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.next)

# -------------------------------
# Example Usage
# -------------------------------

# Create first list: 1 -> 2 -> 3
L = Node(1)
L.next = Node(2)
L.next.next = Node(3)

# Create second list: 4 -> 5
M = Node(4)
M.next = Node(5)

# 1. Find second-to-last node in L
second_last = second_to_last(L)
if second_last:
    print("Second-to-last node data in L:", second_last.data)
else:
    print("List is too short.")

# 2. Concatenate L and M
concatenated = concatenate(L, M)
# Print concatenated list
print("Concatenated list:", end=" ")
current = concatenated
while current:
    print(current.data, end=" ")
    current = current.next
print()

# 3. Count nodes in concatenated list
count = count_nodes(concatenated)
print("Number of nodes in concatenated list:", count)