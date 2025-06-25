# Qn1:
# Divide and conquer splits a problem into smaller subproblems, solves them independently, and combines their results.
# Similar to your other sorts like quick,merge, etc.
# Example: Merge Sort
# Divide: Split the array into two halves.
# Combine: Merge the sorted halves into a single sorted array.


# Qn2: Merge Sort Binary Tree Trace:

# a. [4, 7, 1, 8, 3, 2, 6, 5] (ascending order)
# Splitting:
# [4, 7, 1, 8, 3, 2, 6, 5]
#   /                   \
# [4, 7, 1, 8]       [3, 2, 6, 5]
#  /      \           /      \
# [4,7] [1,8]     [3,2]  [6,5]
# / \    / \       / \    / \
# 4 7   1 8       3 2    6 5

# Merging (ascending):
# [4,7] -> [4,7]
# [1,8] -> [1,8]
# [3,2] -> [2,3]
# [6,5] -> [5,6]
# [4,7,1,8] -> [1,4,7,8]
# [3,2,6,5] -> [2,3,5,6]
# [1,4,7,8,2,3,5,6] -> [1,2,3,4,5,6,7,8]

# b. [5, 2, 7, 8, 1, 4, 6, 3] (descending order)
# Splitting:
# [5, 2, 7, 8, 1, 4, 6, 3]
#   /                   \
# [5, 2, 7, 8]       [1, 4, 6, 3]
#  /      \           /      \
# [5,2] [7,8]     [1,4]  [6,3]
# / \    / \       / \    / \
# 5 2   7 8       1 4    6 3

# Merging (descending):
# [5,2] -> [5,2]
# [7,8] -> [8,7]
# [1,4] -> [4,1]
# [6,3] -> [6,3]
# [5,2,7,8] -> [8,7,5,2]
# [1,4,6,3] -> [6,4,3,1]
# [8,7,5,2,6,4,3,1] -> [8,7,6,5,4,3,2,1]


# Code to test for yourself:
def merge_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], ascending)
    print(f"Left half: {left}")
    right = merge_sort(arr[mid:], ascending)
    print(f"Right half: {right}")
    return merge(left, right, ascending)

def merge(left, right, ascending):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if ascending:
            # Comparing part
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            # Comparing part
            if left[i] >= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
    # Append any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage:
ascending_list = [4, 7, 1, 8, 3, 2, 6, 5]
descending_list = [5, 2, 7, 8, 1, 4, 6, 3]
print("=========ASCENDING ORDER=========")

print("Ascending order:", merge_sort(ascending_list, ascending=True))

print("=========DESCENDING ORDER=========")
print("Descending order:", merge_sort(descending_list, ascending=False))


# How it works:
# It uses two pointers (i for left, j for right).
# It compares the current elements from both lists:
#   - If ascending is True, it appends the smaller element to result.
#   - If ascending is False, it appends the larger element to result.
# It moves the pointer forward in the list from which the element was taken.
# When one list is exhausted, it appends the remaining elements from the other list.
# The result is a single sorted list.
# Qn3:
# What would be the Big O(Time and Space Complexity) for Merge Sort?

# Time Complexity:
# - Best case:    O(n log n)
# - Average case: O(n log n)
# - Worst case:   O(n log n)
# (n = number of elements)

# Space Complexity:
# - O(n) extra space is needed for merging (temporary arrays)


# Qn4:
# In computer science, an in-place algorithm does not need extra space and transforms the input within the same memory.
#
# Are the sorting algorithms discussed so far in-place?
# - Bubble Sort:      Yes, it is in-place (uses only a constant amount of extra space).
# - Selection Sort:   Yes, it is in-place.
# - Insertion Sort:   Yes, it is in-place.
# - Merge Sort:       No, standard merge sort is NOT in-place (it uses extra space for merging).


# Qn5:
# Given a sequence S of n values, each equal to 0 or 1 (e.g. [1, 0, 0, 1, 1, 0]), describe an in-place method for sorting S.
#
# Explanation:
# Since there are only 0s and 1s, we can use a two-pointer approach:
# - Start with one pointer at the beginning (left) and one at the end (right).
# - Move left forward until you find a 1.
# - Move right backward until you find a 0.
# - If left < right, swap S[left] and S[right].
# - Repeat until left >= right.
# This method sorts all 0s to the left and all 1s to the right, using only a constant amount of extra space.

def inplace_sort_zeros_ones(S):
    left, right = 0, len(S) - 1
    while left < right:
        while left < right and S[left] == 0:
            left += 1
        while left < right and S[right] == 1:
            right -= 1
        if left < right:
            S[left], S[right] = S[right], S[left]
            left += 1
            right -= 1
    return S

# Example usage:
# S = [1, 0, 0, 1, 1, 0]
# inplace_sort_zeros_ones(S)
# Output: [0, 0, 0, 1, 1, 1]