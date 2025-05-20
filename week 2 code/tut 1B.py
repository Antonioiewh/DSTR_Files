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
# pretty much the same as for the quesiton above however, the (1, n + 1, 2 ) third parameter ( 2 ) means to step 2:
# for example : [1,2,3,4,5,6,7,8]
# this would mean it will include the first , then 3 , then 5 
#question 4

range(50, 90, 10)

range(8, -10, -2)
# step 10 meaning 50,60,70,80
# range  6,4,2,0,-2,-4,-6,-8

#question 5

def num_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count
# count = 0 as you have not started counting yet, vowels is a string containing all the vowels ( lower and uppercase ). For char will loop through each character in the input text
# if char in vowels means if the char it's checking is in the vowels string, it'd increment the count variable, hence count +=1
# return count returns the value of count
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
# focus on the while loop. while True means it'd run infinitely and will constantly ask for user input ( line = input() ). lines.append(line) will append your input to the list variable called 'lines'
# except EOFError means when this error happens, do nothing which gets you out of the while loop
# Now, as the question asked to output the lines previously entered in reverse, we shall use lies.reverse() which reverses the list 'lines'
# the for loop , for line in lines, print(line) simply loops through each element in lines and prints it out

#question 7

def all_distinct(numbers):
    return len(set(numbers)) == len(numbers)
# Ok , this one is a bit tricky but you should be fine. 
# We will go based of the assumption that numbers is a list of numbers such as [1,1,2,3,4,4].
# Let's focus on len(set(numbers)) this does 2 things. Firstly, it will convert the list into a set, this is very useful as converting a list into  a set will remove any duplicate elements as a set MUST not contain any duplicates
# next we shall focus on len(numbers). This will return the number of elements in the input list.
# the == comparator will determine if the number of elements in the set is the SAME as the number of elements in the input list
# if the no. of elements for both is the same, this means that there are zero duplicates and hence all numbers are distinct from one another.
# if no. is same , it will return true and vice versa

