def main():
    # Compute and print the sum of (1 + 2 + ... + 10)
    print(sum(10))

def sum(x):
    # Assuming x >= 1
    # Base case: if x is 1, return 1
    if x == 1:
        return 1
    # Recursive case: x + sum of numbers from 1 to (x - 1)
    else:
        return x + sum(x - 1)

main()