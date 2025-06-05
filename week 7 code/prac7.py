# A recursive implementation of Binary Search
def recBinarySearch(target, theValues, first, last):
    # If the sequence of values cannot be subdivided further, we are done
    if first > last:  # BASE CASE #1
        return False
    else:
        # Find the midpoint of the sequence
        mid = (first + last) // 2

        # Does the element at the midpoint contain the target?
        if theValues[mid] == target:  # BASE CASE #2
            return theValues

        # or does the target precede the element at the midpoint?
        elif target < theValues[mid]:
            return recBinarySearch(target, theValues, first, mid - 1)

        # or does the target follow the element at the midpoint?
        else:
            return recBinarySearch(target, theValues, mid + 1, last)
        
    
        
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(recBinarySearch(10, test_list, 0, len(test_list) - 1))  # Should return True


def rearrangeEvenOdd(lst):
    # Base case: if the list is empty, return an empty list
    if len(lst) == 0:
        return []

    # Recursive case
    if lst[0] % 2 == 0:  # If the first element is even
        return [lst[0]] + rearrangeEvenOdd(lst[1:])
    else:  # If the first element is odd
        return rearrangeEvenOdd(lst[1:]) + [lst[0]]

# Test the function
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", original_list)
rearranged_list = rearrangeEvenOdd(original_list)
print("Re-arranged List:", rearranged_list)