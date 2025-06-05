def sumDigits(n):
    # Base case: if n is a single-digit number, return n
    if n < 10:
        return n
    # Recursive case: add the last digit to the sum of the remaining digits
    else:
        return n % 10 + sumDigits(n // 10)

# Test the function
print(sumDigits(368))  # Should return 17