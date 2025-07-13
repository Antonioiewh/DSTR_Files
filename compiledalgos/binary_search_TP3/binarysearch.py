def binarySearch( theValues, target ):
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues)
    # Repeatedly subdivide the sequence in half
    # until the target is found
    passes = 0
    print(f"Target:{target}")
    while low <= high:
        
        # Find the midpoint of the sequence
        mid = (low + high) // 2
        passes +=1
        print(f"Pass: {passes}, low: {low}, high: {high}, mid: {mid} ")

        if theValues[mid] == target:

            #print total passes when found 
            print(f"Total passes:{passes}")
            #look for earlier occurences and store current result
            return mid

        # Or is the target before the midpoint?
        elif target < theValues[mid]:
            high = mid -1
        # Or is the target after the midpoint?
        else:
            low = mid + 1
    return -1


def binarySearch_firstoccurence( theValues, target ):
    # Start with the entire sequence of elements
    low = 0
    high = len(theValues)
    # Repeatedly subdivide the sequence in half
    # until the target is found
    passes = 0
    print(f"Target:{target}")
    while low <= high:
        
        # Find the midpoint of the sequence
        mid = (low + high) // 2
        passes +=1
        print(f"Pass: {passes}, low: {low}, high: {high}, mid: {mid} ")

        if theValues[mid] == target:

            #print total passes when found 
            #look for earlier occurences and store current result
            result = mid
            #continue searching left half to get index of FIRST OCCURENCE if doesnt work, that means you're already at the first occurence
            high = mid - 1 
            
        # Or is the target before the midpoint?
        elif target < theValues[mid]:
            high = mid -1
        # Or is the target after the midpoint?
        else:
            low = mid + 1
    
    return result


print('Binary search test\n-----------------------------')
testlist= [1,2,2,2,3,4,5,6]
print(binarySearch(testlist,2))


print('Binary search first occurence of.. test\n-----------------------------')
print(binarySearch_firstoccurence(testlist,2))