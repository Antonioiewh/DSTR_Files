def exp(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

# Test the function
print(exp(2, 8))  # Should return 256
print(exp(3, 4))  # Should return 81