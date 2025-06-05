def main():
    y = foo(4)
    bar(2)

def foo(x):
    if x % 2 != 0:
        return 0
    else:
        return x + foo(x - 1)

def bar(n):
    if n > 0:
        bar(n - 1)
        print(n)

main()

# a) the output of the program is is 1 and 2
# b) The Big O time complexity is O(n) and the space complexity is O(n) - foo(x)
# c) The Big O time complexity is O(k) and the space complexity is O(k) - bar(n)