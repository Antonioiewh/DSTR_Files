# Sort a sequence in ascending order using the selection sort
# algorithm
def selectionSort( theSeq ):
    n = len( theSeq )
    for i in range(n - 1):
    # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
        # Swap the ith value and smallNdx value only if the
        # smallest value is not already in its proper position.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq
# Test codes

def selection_sort_advanced ( theSeq, parameter):

    n = len( theSeq )
    for i in range(n - 1):
    # Assume the ith element is the smallest.
        smallNdx = i
        # Determine if any other element contains a smaller value.
        for j in range(i+1, n):
            if parameter == "A":
                if theSeq[j] < theSeq[smallNdx]:
                    smallNdx = j
            elif parameter == "D":
                if theSeq[j] > theSeq[smallNdx]:
                    smallNdx = j
        # Swap the ith value and smallNdx value only if the
        # smallest value is not already in its proper position.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
    return theSeq
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]


print(f'Sorted in Ascending Order:\nInput List: {list_of_numbers}\nOutput List: {selectionSort(list_of_numbers)}\n')
print(f'Sorted in Descending Order:\nInput List: {list_of_numbers}\nOutput List: {selection_sort_advanced(list_of_numbers, "D")}\n')