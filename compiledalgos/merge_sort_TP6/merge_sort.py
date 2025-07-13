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