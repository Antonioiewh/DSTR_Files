def custom_sort(strings):
    # Separate strings that start with 'H' and others
    h_strings = [s for s in strings if s.startswith('H')]
    other_strings = [s for s in strings if not s.startswith('H')]
    
    # Sort both lists
    h_strings_sorted = sorted(h_strings)
    other_strings_sorted = sorted(other_strings)
    
    # Combine the lists with 'H' strings first
    return h_strings_sorted + other_strings_sorted

# Example usage
input_list = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
output_list = custom_sort(input_list)
print(output_list)