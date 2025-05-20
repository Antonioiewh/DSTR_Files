# using reverse indexing
list = [1, 2, 3, 4, 5]
print(list[::-1])  # Output: [5, 4, 3, 2, 1]
#Explanation
# First we must understand what :: means
# It means start from and the step size (so if the step size is 2 you're skipping every 2nd element)
# So in this case we are starting from the end of the list and going backwards
# So the output is [5, 4, 3, 2, 1]
# To and fro, if to -> exclude it, if fro-> include it


# Example 
print(f'Example 1 with it being list [::-2]: {list[::-2]}')  # Output: [5, 3, 1]
# Explanation
# Include element at index -2 and skip over every 2nd element when going backwards 

# Example 2
print(f'Example 2 with it being list [-2::]: {list[-2::]}')   # Output: [1, 3, 5]
# Explanation
# Include element at index -2 and skip over every 2nd element when going backwards 

# Example 3
print(f'Example 3 with it being list [::2]: {list[::2]}')

#Example 3
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