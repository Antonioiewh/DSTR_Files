# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimised(theSeq):
    n = len(theSeq)
    num_passes = 0
    print("Initial list:", theSeq)
    for i in range(n - 1, 0, -1):
        swap = False
        for j in range(i):
            # Check if the keys are equal before swapping
            if theSeq[j][1] == theSeq[j + 1][1]:
                print(f"Equal keys found at positions {j} and {j+1}: {theSeq[j]} and {theSeq[j+1]} (no swap needed for stability)")
            if theSeq[j][1] > theSeq[j + 1][1]:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                swap = True
        num_passes += 1
        # If no swaps were made, the sequence is sorted
        if not swap:
            print(f"No swaps needed, sequence is sorted after {num_passes + 1} passes.")
            break
        
        print(f"After pass {num_passes}: {theSeq}")
    print(f"Number of passes is {num_passes}")
    return theSeq


def bubbleSort(theSeq):
    n = len(theSeq)
    num_passes = 0
    print("Initial list:", theSeq)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            # Check if the keys are equal before swapping
            if theSeq[j][1] == theSeq[j + 1][1]:
                print(f"Equal keys found at positions {j} and {j+1}: {theSeq[j]} and {theSeq[j+1]} (no swap needed for stability)")
            if theSeq[j][1] > theSeq[j + 1][1]:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
        num_passes += 1
        print(f"After pass {num_passes}: {theSeq}")
    print(f"Number of passes is {num_passes}")
    return theSeq

unsorted_list = [('A', 5), ('B', 2), ('C', 3), ('D', 1), ('E', 2)]
sorted_list = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 2)]
print('Using optimised:')
print(f"Unsorted: {bubbleSort_optimised(unsorted_list)}")
print(f"Sorted: {bubbleSort_optimised(sorted_list)}")
print('Using unoptimised:')
print(f"Unsorted: {bubbleSort(unsorted_list)}")
print(f"Sorted: {bubbleSort(sorted_list)}")




# No. of passes: The standard bubble sort always performs n-1 passes, where n is the length of the list.
# Space complexity is O(1), time complexity is O(n^2)
# Stability : Yes as it only swaps when the first key is strictly greater than the second key