class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head, msg="Current list"):
    """Prints the current state of the linked list."""
    elems = []
    cur = head
    while cur is not None:
        elems.append(str(cur.data))
        cur = cur.next
    print(f"{msg}: {' -> '.join(elems) if elems else 'Empty'}")

def append(head, data):
    """Append a node with the given data to the end of the list."""
    print(f"Appending {data} to list.")
    new_node = ListNode(data)
    if head is None:
        print_list(new_node, "After append")
        return new_node
    cur = head
    while cur.next is not None:
        cur = cur.next
    cur.next = new_node
    print_list(head, "After append")
    return head

def traversal(head):
    """Traverse and print all nodes in the list."""
    print("Traversing list:")
    curNode = head
    while curNode is not None:
        print(f"  Visited node: {curNode.data}")
        curNode = curNode.next

def unorderedSearch(head, target):
    """Search for a node with the target value."""
    print(f"Searching for {target} in list.")
    curNode = head
    while curNode is not None and curNode.data != target:
        print(f"  Visited: {curNode.data}")
        curNode = curNode.next
    if curNode is not None:
        print(f"  Found: {curNode.data}")
        return True
    else:
        print("  Not found")
        return False

def delete(head, target):
    """Delete the first node with the target value."""
    print(f"Deleting {target} from list.")
    if head is None:
        print("  List is empty.")
        return None
    if head.data == target:
        print(f"  Deleted head node with value {target}.")
        print_list(head.next, "After delete")
        return head.next
    prev = head
    cur = head.next
    while cur is not None:
        if cur.data == target:
            print(f"  Deleted node with value {target}.")
            prev.next = cur.next
            print_list(head, "After delete")
            return head
        prev = cur
        cur = cur.next
    print("  Value not found; nothing deleted.")
    print_list(head, "After delete")
    return head

# Example usage:
if __name__ == "__main__":
    # Create linked list: 6 -> 7 -> 8
    head = ListNode(6)
    print_list(head, "Initial list")
    head = append(head, 7)
    head = append(head, 8)
    print_list(head, "List after appends")
    print("Traversal:")
    traversal(head)
    print("Search for 7:")
    unorderedSearch(head, 7)
    print("Delete 7 and traverse:")
    head = delete(head, 7)
    traversal(head)
    print_list(head, "Final list")