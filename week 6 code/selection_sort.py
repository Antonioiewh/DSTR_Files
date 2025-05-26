#selection sort descending
# video useful https://www.youtube.com/watch?v=EwjnF7rFLns, the code is not in python so dont worry
testarr = [12,7,9,24,7,29,5,3,11,7]
def selection_sort_descending(arr):
    n = len(arr)
    passes = 0
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Test against elements after i to find the smallest
        for j in range(i + 1, n):
            if arr[j] > arr[min_index]: #this changes desc/asc 
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        passes += 1
        print(f"Pass {passes}: {arr}")
    
    return arr



# one cycle should be:
# look at first element, ill then find the smalest element and swap it with the first
# then look at the second element, ill find the smalest element and swap it with the second
# cycle repeats



def selection_sort_ascending(arr):
    n = len(arr)
    passes = 0
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        # Test against elements after i to find the smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]: #this changes desc/asc
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        passes += 1
        print(f"Pass {passes}: {arr}")


# insetion sort descending

def insertion_sort_descending(arr):
    n = len(arr)
    passes = 0
    for i in range(1, n): # starts from second element
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:  # this changes desc/asc
            arr[j + 1] = arr[j] # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
            j -= 1
        arr[j + 1] = key
        passes += 1
        print(f"Pass {passes}: {arr}")
    return arr

# insertion sort ascending
# useful video https://www.youtube.com/watch?v=8mJ-OhcfpYg 
def insertion_sort_ascending(arr):
    n = len(arr)
    passes = 0
    for i in range(1, n): # starts from second element
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # this changes desc/asc
            arr[j + 1] = arr[j] # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
            j -= 1
        arr[j + 1] = key
        passes += 1
        print(f"Pass {passes}: {arr}")
    return arr


#print(selection_sort_descending(testarr))
#print(selection_sort_ascending(testarr))
print(insertion_sort_descending(testarr))
#print(insertion_sort_ascending(testarr))

#Qn2a: True. As seen from the output, the Number of passes is equal to the number of sorted elements
#Qn2b: True. Folllowing the same principle, it should be the same
