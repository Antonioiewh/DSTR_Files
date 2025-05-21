# using reverse indexing
list = [1, 2, 3, 4, 5]
print(list[::-1])  # Output: [5, 4, 3, 2, 1]
#Explanation
# First we must understand what :: means
# It means start from and the step size (so if the step size is 2 you're skipping every 2nd element)
# So in this case we are starting from the end of the list and going backwards
# So the output is [5, 4, 3, 2, 1]
# For [::] cases:
# If element in front: print till end
# If element at back: print till start plus skip over every X elements
# To and fro, if to -> exclude it, if fro-> include it


# Examples 
print(f'Example 1 with it being list [::-2]: {list[::-2]}')  
# Explanation
# Include element at index -2 and skip over every 2nd element when going backwards 

# Example 2
print(f'Example 2 with it being list [-2::]: {list[-2::]}')   
# Explanation
# Start at element at at index -2 and print til end

# Example 3
print(f'Exaple 3 with it being list [:-2] {list[:-2]}')
# Print till element at index -2
# Example 4
print(f'Exaple 4 with it being list [-2:] {list[-2:]}')
# Explanation 
# Start at element at index -2, print till end

# Example 5
print(f'Example 5 being list [-2::-2] {list[-2::-2]}')
# Explanation
# Start at index -2, step by -2 
# Example 6
print(f'Example 5 being list [-2::-2] {list[-2::2]}')
# Start at index -2, step by 2

# Example 7
print(f'Example 7 with it being list [::2]: {list[::2]}')
# Explanation
# Include element at index 2 and skip over every 2nd element when going backwards

#Example 8
print(f'Example 8 with it being list[2::] {list[2::]}')
# Explanation
# Include element at index 2 and print til end

#Example 9
print(f'Example 9 with it being list[:2] {list[:2]}')
# Explanation
# Print till element at 2


#Example 10
print(f'Example 11 with it being list[2:] {list[2:]}')
# Explanation
# Start at element at index 2 , print till end


#Example 11
#Turn "the quick brown fox!!" turn into "quick brown fox!"
#Options ( multi select)
# [4:-1:-1]
#[-17:-1]
#[-17:-1:1]
#[-4:-1:1]
#[4:-1:1]



#Answers: [4:-1:1], [-17:-1:1], [-17:-1]
# Explanation you can't do [x:y:z], it straight up is criminal
original = "the quick brown fox!!"

#Ans 1
print(original[4:-1:1]) # same as [4:-1] exclude the last '!'

#Ans 2
print()
