# structured
array = [1, 2, 3]

def recursion(array, index=0):
    """
    For each element in array:
    - Base case: if element > 7, stop processing that element
    - Otherwise: calculate (element - 1) + len(array) until element > 7
    - Move to next element in array
    """
    # Base case: processed all elements in array
    if index >= len(array):
        return []
    
    # Get current element
    current_element = array[index]
    print(f"Processing element at index {index}: {current_element}")
    
    # Process current element until next iteration would be > 7
    def process_element(element):
        # Calculate what the next value would be
        next_value = (element - 1) + len(array)
        print(f"  {element}: next would be ({element} - 1) + {len(array)} = {next_value}")
        
        # Base case: if next_value > 7, return current element
        if next_value > 7:
            print(f"  Base case: next value {next_value} > 7, so return current {element}")
            return element
        else:
            # Continue with the next value
            return process_element(next_value)
    
    # Process current element
    result = process_element(current_element)
    
    # Move to next element and combine results
    remaining_results = recursion(array, index + 1)
    return [result] + remaining_results

# Test the function
print("Array:", array)
print("Results:", recursion(array))