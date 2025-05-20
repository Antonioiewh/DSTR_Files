#qustion 1

def minmax(data):
    small = big = data[0]  # assuming data is non-empty

    for value in data:
        if value < small:
            small = value
        elif value > big:
            big = value

    return (small, big)
#NOT allowed to use min max so we will use this instead
# First statement assigns dta[0] to BOTH small and big variables as obviously you need something to compare with 
# Next you wil check through the data list
# if value < small , small = vlaue means if value less than variable small, you will proceed to pass the current value you're looking at into the variable small
# if value > big , big = vlaue means if value larger than variable big, you will proceed to pass the current value you're looking at into the variable big
#qestion 2
def sum_of_squares(n):
    total = 0
    for j in range(1, n + 1):
        total += j * j
    return total

print(sum_of_sqaures(n)) 
# first assign value of total var = 0
# for j in range (1 n + 1) means looking at values less or equal. n+1 allows you to look at the value n as n+1 is the limit. 
# total += j*j means you will calculate the square of j and add it to total
# you need to use print() to display the value of total from the function

def sum_of_squares(n):
    total = 0
    for j in range(1, n + 1, 2):
        total += j * j
    return total

#question 4

range(50, 90, 10)

range(8, -10, -2)


#question 5

def num_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count

#question 6

lines = []
try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass

lines.reverse()
for line in lines:
    print(line)

#question 7

def all_distinct(numbers):
    return len(set(numbers)) == len(numbers)


