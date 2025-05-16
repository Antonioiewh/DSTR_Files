#qustion 1

def minmax(data):
    small = big = data[0]  # assuming data is non-empty

    for value in data:
        if value < small:
            small = value
        elif value > big:
            big = value

    return (small, big)

#qestion 2
def sum_of_squares(n):
    total = 0
    for j in range(1, n + 1):
        total += j * j
    return total

#question 3
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


