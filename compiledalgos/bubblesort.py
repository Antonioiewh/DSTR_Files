# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized( theSeq ):
    n = len( theSeq )
    num_passes = 0
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        swapped = False
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
            # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                # Set boolean variable value if swapping occurred

                swapped = True
        num_passes +=1
        # Exit the loop if no swapping occurred
        # in the previous pass
        if swapped == False:
            break
    return f"Number of passes is {num_passes}"
    


# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort( theSeq ):
    n = len( theSeq )
    num_passes = 0
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
            # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                # Set boolean variable value if swapping occurred

        num_passes +=1

    return f"Number of passes is {num_passes}"
    

#test it works

unsorted_list = [1, 2, 3, 5, 4]
sorted_list = [1,2,3,4,5]
print('Using optimised:')
print(bubbleSort_optimized(unsorted_list))
print(bubbleSort_optimized(sorted_list))
print('Using unoptimised:')
print(bubbleSort(unsorted_list))
print(bubbleSort(sorted_list))

# Qn1b:How many pass(es) is(are) required to sort the following list of numbers with the
# standard Bubble Sort and the optimized Bubble Sort?
# [ 1, 2, 3, 5, 4 ]
# Standard: 4
# Optimised: 2
#Explanation: The standard bubble sort always performs n-1 passes, where n is the length of the list.
# For [1, 2, 3, 5, 4] (n=5)
# However, the optimised bubble sort stops early if no swaps are not needed in the outer for loop which MEANS that it is already sorted
# Hence after the 2nd pass, it determines it's sorted and breaks out from the outer loop. Hence the number of pases is 2
#Qn1c: 1 passes as it needs ONE pass to determine it is already sorted which will cause it end the for loop 

#Qn2: Space complexity is O(1), time complexity is O(n^2)