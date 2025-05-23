my_string = "this is python Programing."

print(my_string.replace(" ","")) #<<modify codes>>


"""Output:
thisispythonPrograming."""
#Explaination: replaces spaces " " with nothing "" aka removing them 

my_string = "this is python Programing"
print(my_string[-17:-10]) #<<modify codes>>
"""Output:
python"""
#Explaination: -17 is at 'p' goes to -10 and excludes it
my_list = [100, 100.5, 30, 70, 125.6, 'Python', 'Java',
'Ruby']
my_list.insert(4,77) #<< modify codes>>
print(my_list)
"""output:
[100, 100.5, 30, 70, 77, 125.6, 'Python', 'Java', 'Ruby']"""
#Explaination: insert 77 at index 4 and the rest move to the right

my_list1 = [100, 100.5, 30, 70, 125.6, 109.25, 101.01, 209.99]

desc = sorted(my_list1,reverse=True) #<< modify codes>>
print(desc)
"""Output:
[209.99, 125.6, 109.25, 101.01, 100.5, 100, 70, 30]"""
#Use sorted() not list.sort. list.sort will return a new instance of it being sorted causing your original list to not be affected.

my_list2 = [100, 100.5, 30, 70, 125.6, 'Python', 'Java',
'Ruby']
my_slice = my_list2[:-4]#<< modify codes>>
print(my_slice)
"""Output:
[100, 100.5, 30, 70]"""
#Explanation: this gives you all elements except last 4

programming = {1: "Java", 2: "C", 3: "C++", 4: "R", 5:
"Python"}

verify = (6 in programming)#<< modify codes>>

print(verify) 
#Explanation, verifies if the key 6 is in the dictionary 'programming'. If not in, return False and vice versa. print() will print out True or False.

programming = {1: "Java", 2: "C", 3: "C++", 4: "R", 5:
"Python"}
val = programming.values()#<< modify codes>>
print(list(val))


programming = {1: "Java", 2: "C#", 3: "C++", 4: "R", 5:
"Python", 6: "Javascript"}
#<< modify codes>>

if len(min(programming.values())) == programming[6].count('a'):
    print("True!")
else:
    print("false")

# First focus on (min(programming.values()), it retrieves the key with the lowest value. 
# Secondly, programming[6], 6 is the key while .count('') returns the count of the letter
# Thirdly len(min(programming.values()) gets the number of letters in the lowest value
# Lastly the if statement asks if the number of letters in the lowest value is equal to the number of times the letter 'a' appears in the value of key 6 
x = [2, 4, 6, 8]
y = [5, 10, 15, 20]

for i in x:
    for j in y:
        if i > 5 and j < 12:
            print(i*j)

"""Output:
30
60
40
80"""
# A nested for loop is used as the question states mulitply each value of X with Y which suggests the first loop will be X and 2nd being Y
# For I in X i will then compare with EACH AND EVERY SINGLE element of y 
# the if statement is pretty self explanatory with there being 2 conditions that MUST be fulfilled being the element in X must be greater than 5 and element in Y must be lesser than 12
# if both conditions are met, print out the product of the element in X and Y 

var = 8
def my_func(x):
    global var
    print(x * var)
    var = 12
    
my_func(10)
#global var means you're USING THE GLOBAL VARIABLE AKA THE ONE NOT IN THE FUNCTION this will allow you to directly alter the values of the global variables
# var = 12 wont affect the output as it's AFTER the print line
