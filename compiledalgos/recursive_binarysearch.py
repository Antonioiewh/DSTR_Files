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