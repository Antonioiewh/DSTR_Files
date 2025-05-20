original = "the quick brown fox!!"
# Remove "the " at the start (first 4 chars), and one "!" at the end
result = original [4:-1:-1]
print(result)  # Output: quick brown fox!
# Answer: [-17:-1:1], [-117:-1] and [4:-1] correct answers
# ignore the last character which is ":1" and work from there
def add(a,b):
    return a+5,b+5

print(add(3,4))
# Answer: (8, 9)

#All instances of a class share the same value. While all instances of a instance are independent and do not share value
#True or False
#Answer: False as all instances of a class share the same attributes BUT not values 
def sum_of_squares(n):
    total = 0
    for j in range(1, n + 1):
        total += j * j
    return total

print(sum_of_squares(3))


def all_distinct(numbers):
    return len(set(numbers)) == len(numbers)

print(all_distinct([1, 2,2, 3, 4, 5]))  # True