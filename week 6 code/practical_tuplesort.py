def sort_by_last_element(tuples):
    # Sort the list of tuples using the last element of each tuple as the key
    return sorted(tuples, key=lambda x: x[-1])

# Example usage
input_list = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
output_list = sort_by_last_element(input_list)
print(output_list)