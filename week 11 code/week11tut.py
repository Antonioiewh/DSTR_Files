# Q1: Quick Sort Binary Tree Trace (using first element as pivot)

# a. [4, 7, 1, 8, 3, 2, 6, 5] (ascending order)
# Step 1: Choose 4 as pivot
#   Left: [1, 3, 2]   Pivot: 4   Right: [7, 8, 6, 5]
# Step 2: Sort left [1, 3, 2] (pivot 1)
#   Left: []   Pivot: 1   Right: [3, 2]
#   Sort [3, 2] (pivot 3): Left: [2] Pivot: 3 Right: []
# Step 3: Sort right [7, 8, 6, 5] (pivot 7)
#   Left: [6, 5]   Pivot: 7   Right: [8]
#   Sort [6, 5] (pivot 6): Left: [5] Pivot: 6 Right: []
# Step 4: Combine all:
#   [1, 2, 3] + 4 + [5, 6, 7, 8] = [1, 2, 3, 4, 5, 6, 7, 8]

# b. [5, 2, 7, 8, 1, 4, 6, 3] (descending order)
# Step 1: Choose 5 as pivot
#   Left: [2, 1, 4, 3]   Pivot: 5   Right: [7, 8, 6]
# Step 2: Sort right [7, 8, 6] (pivot 7)
#   Left: [6]   Pivot: 7   Right: [8]
#   Sort [8]: already sorted
# Step 3: Sort left [2, 1, 4, 3] (pivot 2)
#   Left: [1]   Pivot: 2   Right: [4, 3]
#   Sort [4, 3] (pivot 4): Left: [3] Pivot: 4 Right: []
# Step 4: Combine all in descending order:
#   [8, 7, 6] + 5 + [4, 3, 2, 1] = [8, 7, 6, 5, 4, 3, 2, 1]

# Code below:
def quick_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    if ascending:
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
    else:
        left = [x for x in arr[1:] if x > pivot]
        right = [x for x in arr[1:] if x <= pivot]
    print(f"Pivot: {pivot}, Left: {left}, Right: {right}")
    return quick_sort(left, ascending) + [pivot] + quick_sort(right, ascending)

# Example usage:
ascending_list = [4, 7, 1, 8, 3, 2, 6, 5]
descending_list = [5, 2, 7, 8, 1, 4, 6, 3]

print("========ASCENDING ORDER========")
print("Ascending order:", quick_sort(ascending_list, ascending=True))
print("========DESCENDING ORDER========")
print("Descending order:", quick_sort(descending_list, ascending=False))

# Q2:  Big O for Quick Sort (Time and Space Complexity):
# Time Complexity:
# - Best Case: O(n log n) when the pivot divides the array into two equal halves.
# - Average Case: O(n log n) for random distributions.
# - Worst Case: O(n^2) when the pivot is the smallest or largest element repeatedly (e.g., already sorted array).
# Space Complexity:
# - O(log n) for the recursive stack space in the best and average cases.

# Q3: Stability of Sorting Algorithms:
# A stable sort keeps the relative order of records with equal keys (values) the same as in the original list.
# Bubble Sort: Stable
'''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
'''
# Example: [(2, 'A'), (1, 'B'), (2, 'C')]
# Output: [(1, 'B'), (2, 'A'), (2, 'C')]  # 'A' stays before 'C'
# Selection Sort: Not Stable
'''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j][0] < arr[min_idx][0]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
'''
# Example: [(2, 'A'), (1, 'B'), (2, 'C')]
# Output: [(1, 'B'), (2, 'C'), (2, 'A')]  # 'C' comes before 'A'
# Insertion Sort: Stable
'''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
'''
# Example: [(2, 'A'), (1, 'B'), (2, 'C')]
# Output: [(1, 'B'), (2, 'A'), (2, 'C')]
# Merge Sort: Stable
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
'''
# Example: [(2, 'A'), (1, 'B'), (2, 'C')]
# Output: [(1, 'B'), (2, 'A'), (2, 'C')]
# Quick Sort: Not Stable
'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0][0]
    left = [x for x in arr[1:] if x[0] < pivot]
    right = [x for x in arr[1:] if x[0] >= pivot]
    return quick_sort(left) + [arr[0]] + quick_sort(right)
'''
# Example: [(2, 'A'), (1, 'B'), (2, 'C')]
# Output: [(1, 'B'), (2, 'C'), (2, 'A')]  # 'C' comes before 'A'

# 4. One Similarity and One Difference between Merge Sort and Quick Sort:
# Similarity:
# Both are divide and conquer algorithms with average time complexity O(n log n).
# Difference:
# Merge Sort is stable and requires O(n) additional space, while Quick Sort is not stable and can be done in-place with O(log n) space complexity for the recursive stack.