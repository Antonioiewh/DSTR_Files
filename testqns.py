original = "the quick brown fox!!"
# Remove "the " at the start (first 4 chars), and one "!" at the end
result = original [4:-1:-1]
print(result)  # Output: quick brown fox!
# Answer: [-17:-1:1],[-17:-1], and [4:-1] correct answers
# ignore the last character which is ":1" and work from there
def add(a,b):
    return a+5,b+5

print(add(3,4))
# Answer: (8, 9)

#All instances of a class share the same value. While all instances of a instance are independent and do not share value
#True or False
#Answer: False as all instances of a class share the same attributes BUT not values 
