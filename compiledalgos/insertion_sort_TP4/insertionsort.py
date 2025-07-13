# Sorts a sequence in ascending order using the insertion sort
# algorithm and displays stability information
def insertionSort(theSeq):
    print("Insertion Sort Algorithm")
    n = len(theSeq)
    passes = 0
    for i in range(1, n):
        value = theSeq[i][1]
        label = theSeq[i][0]
        pos = i
        print(f"pos = {theSeq[pos]}")
        # Check for stability: if equal values, print their labels
        while pos > 0 and value < theSeq[pos - 1][1]:
            if value == theSeq[pos - 1][1]:
                print(f"Stability: {theSeq[pos-1]} and ({label}, {value}) have equal values. Original order preserved.")
            # Shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos -= 1
        # Put the saved value into the open slot.
        theSeq[pos] = (label, value)
        passes += 1
        print(f"Pass {passes}: {theSeq}")

# Test codes
list_of_numbers = [('A',10), ('B',51), ('C',4), ('D',18), ('E',4)]
print('Input List:', list_of_numbers)
insertionSort(list_of_numbers)
print('Sorted List:', list_of_numbers)