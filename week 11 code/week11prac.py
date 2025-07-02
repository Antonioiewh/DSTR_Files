def recQuickSort(theList, first, last):
    if first >= last:
        return
    else:
        pos = partitionSeq(theList, first, last)
        print(f"After partitioning with pivot at index {pos}: {theList}")
        recQuickSort(theList, first, pos - 1)
        recQuickSort(theList, pos + 1, last)

def quickSort(theList):
    n = len(theList)
    recQuickSort(theList, 0, n-1)

def partitionSeq(theList, first, last):
    pivot = theList[first]
    left = first + 1
    right = last
    print(f"\nPartitioning: {theList[first:last+1]}, pivot={pivot} (index {first})")
    while left <= right:
        print(f"  Left marker: left = {left}, Right marker: right = {right}")
        while left <= right and theList[left] < pivot:
            left += 1
            print(f"    Moved left marker to left = {left}")
        while left <= right and theList[right] > pivot:
            right -= 1
            print(f"    Moved right marker to right = {right}")
        if left <= right:
            print(f"  Swapping {theList[left]} (index {left}) and {theList[right]} (index {right})")
            theList[left], theList[right] = theList[right], theList[left]
            left += 1
            right -= 1
    print(f"  Swapping pivot {theList[first]} (index {first}) with {theList[right]} (index {right})")
    theList[first], theList[right] = theList[right], theList[first]
    print(f"  Result after partition: {theList[first:last+1]}")
    return right

list_of_numbers = [4, 7, 2, 8, 3, 1, 6, 5]
print('Input List:', list_of_numbers)
quickSort(list_of_numbers)
print('Sorted List:', list_of_numbers)
# Let's walk through the partitionSeq function step by step with your list:
#
# theList = [4, 7, 2, 8, 3, 1, 6, 5]
# first = 0
# last = 7
# pivot = theList[first] = 4
# left = 1
# right = 7
#
# Step-by-step trace
#
# Initial state:
# Indexes:   0  1  2  3  4  5  6  7
# List:     [4, 7, 2, 8, 3, 1, 6, 5]
#            ^                    ^
#         pivot                 right
#         left
#
# 1. Move left and right pointers:
# - left at 1 (7 > 4, stop)
# - right at 7 (5 > 4, right -= 1 → 6)
# - right at 6 (6 > 4, right -= 1 → 5)
# - right at 5 (1 < 4, stop)
#
# 2. Swap left and right:
# - Swap theList[1] and theList[5] (7 and 1)
# - List becomes: [4, 1, 2, 8, 3, 7, 6, 5]
# - left += 1 → 2, right -= 1 → 4
#
# 3. Move pointers again:
# - left at 2 (2 < 4, left += 1 → 3)
# - left at 3 (8 > 4, stop)
# - right at 4 (3 < 4, stop)
#
# 4. Swap left and right:
# - Swap theList[3] and theList[4] (8 and 3)
# - List becomes: [4, 1, 2, 3, 8, 7, 6, 5]
# - left += 1 → 4, right -= 1 → 3
#
# 5. Now left > right (4 > 3), exit loop.
#
# 6. Place pivot:
# - Swap theList[first] and theList[right] (4 and 3)
# - List becomes: [3, 1, 2, 4, 8, 7, 6, 5]
# - Pivot is now at index 3
#
# Final state after partitionSeq:
# [3, 1, 2, 4, 8, 7, 6, 5]
#              ^
#            pivot (index 3)
# - All elements left of index 3 are less than pivot (4)
# - All elements right of index 3 are greater than pivot (4)
#
# This is exactly how your code works for this