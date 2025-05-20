original = "the quick brown fox!!"

# Examples 
print(f'Example 1 with it being original[::-2]: {original[::-2]}')  # Output: [5, 3, 1]
# Explanation
# Include element at index -2 and skip over every 2nd element when going backwards 

# Example 2
print(f'Example 2 with it being original[-2::]: {original[-2::]}')   # Output: [1, 3, 5]
# Explanation
# Include element at index -2 and print til end

# Example 3
print(f'Exaple 3 with it being orignal[:-2] {original[:-2]}')
#Explanation start from the element after -2 which is 3 till the end

# Example 4
print(f'Exaple 4 with it being orignal[:-2] {original[-2:]}')
#Explanation start from element at -2 till the end


# Example 5
print(f'Example 3 with it being original[::2]: {original[::2]}')
# Explanation
# Include element at index 2 and skip over every 2nd element when going backwards

#Example 6
print(f'Example 6 with it being original[2::] {original[2::]}')
# Explanation
# Include element at index 2 and print til end

#Example 7
print(f'Example 7 with it being original[:2] {original[:2]}')
# Explanation
# Exclude element at index 2 and print till end


#Example 8
print(f'Example 8 with it being original[2:] {original[2:]}')
# Explanation
# Include element at index 2 and print till end

