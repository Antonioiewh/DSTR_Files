# Sort a sequence in ascending order using the selection sort algorithm

def selectionSort(theSeq):
    n = len(theSeq)  # Get the length of the sequence
    for i in range(n - 1):  # Loop through each element except the last
        smallNdx = i  # Assume the current position holds the smallest value
        # Find the index of the smallest value in the unsorted part
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        # Swap if a smaller value was found
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq  # Return the sorted sequence

# Advanced selection sort that can sort in ascending or descending order
def selection_sort_advanced(theSeq, parameter):
    n = len(theSeq)
    for i in range(n - 1):
        smallNdx = i  # Assume the current position is the smallest/largest
        for j in range(i + 1, n):
            if parameter == "A":  # Ascending order
                if theSeq[j] < theSeq[smallNdx]:
                    smallNdx = j
            elif parameter == "D":  # Descending order
                if theSeq[j] > theSeq[smallNdx]:
                    smallNdx = j
        # Swap if a new smallest/largest value was found
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq  # Return the sorted sequence

# Test code
unsorted_list = [('A', 5), ('B', 2), ('C', 3), ('D', 1), ('E', 2)]
sorted_list = [('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 2)]
print("Unsorted list:", unsorted_list)
print("Sorted list (ascending):", selectionSort(unsorted_list.copy()))
print("Sorted list (descending):", selection_sort_advanced(unsorted_list.copy(), "D"))
