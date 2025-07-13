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

# Sorts an array or list using the recursive quick sort algorithm
def quickSort(theSeq, ascending=True):
    n = len(theSeq)
    recQuickSort(theSeq, 0, n - 1, ascending)

# The recursive "in-place" implementation
def recQuickSort(theSeq, first, last, ascending):
    # Check the base case (range is trivially sorted)
    if first >= last:
        return
    else:
        # Partition the sequence and obtain the pivot position
        pos = partitionSeq(theSeq, first, last, ascending)
        print(f"After partition: {theSeq[first:last+1]}, Pivot index: {pos}, Pivot value: {theSeq[pos]}")
        # Repeat the process on the two subsequences
        recQuickSort(theSeq, first, pos - 1, ascending)
        recQuickSort(theSeq, pos + 1, last, ascending)

# Partitions the subsequence using the first key as the pivot
def partitionSeq(theSeq, first, last, ascending):
    pivot = theSeq[first]
    left = first + 1
    right = last
    print(f"Partitioning: {theSeq[first:last+1]}, Pivot: {pivot}")
    while left <= right:
        if ascending:
            while left <= right and theSeq[left] < pivot:
                left += 1
            while left <= right and theSeq[right] > pivot:
                right -= 1
        else:
            while left <= right and theSeq[left] > pivot:
                left += 1
            while left <= right and theSeq[right] < pivot:
                right -= 1
        if left <= right:
            print(f"  Swapping {theSeq[left]} and {theSeq[right]}")
            theSeq[left], theSeq[right] = theSeq[right], theSeq[left]
            left += 1
            right -= 1
    theSeq[first], theSeq[right] = theSeq[right], pivot
    print(f"  Placing pivot {pivot} at index {right}: {theSeq[first:last+1]}")
    return right

ascending_list = [4, 7, 1, 8, 3, 2, 6, 5]
descending_list = [5, 2, 7, 8, 1, 4, 6, 3]

print("========ASCENDING ORDER========")
arr1 = ascending_list.copy()
quickSort(arr1, ascending=True)
print("Ascending order:", arr1)

print("========DESCENDING ORDER========")
arr2 = descending_list.copy()
quickSort(arr2, ascending=False)
print("Descending order:", arr2)