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
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

# Print sorted list in ascending order
print(f'Sorted in Ascending Order:\nInput List: {list_of_numbers}\nOutput List: {selectionSort(list_of_numbers)}\n')
# Print sorted list in descending order
print(f'Sorted in Descending Order:\nInput List: {list_of_numbers}\nOutput List: {selection_sort_advanced(list_of_numbers, "D")}\n')