def sortedsequentialsearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        #its sorted so this shouldnt happen but whatever
        elif theValues[i] > target:
            return False
    return False



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


def binarySearchC( theValues, target ):
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
testlist= [1,2,3,4,5,6,7,8,9]
print(binarySearch(testlist,9))
print(binarySearch(testlist,1))

print('Binary searchC test\n-----------------------------')
testlistC = [1,2,2,2,3,4,5,6]
print(binarySearchC(testlistC,2))