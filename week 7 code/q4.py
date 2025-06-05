def isPalindrome(aStr):
    # Base case: if the string has 0 or 1 character, it is a palindrome
    if len(aStr) <= 1:
        return True
    # Recursive case: check if the first and last characters are the same
    # and recursively check the substring excluding the first and last characters
    elif aStr[0] == aStr[-1]:
        return isPalindrome(aStr[1:-1])
    else:
        return False

# Test the function
print(isPalindrome("madam"))  # Should return True
print(isPalindrome("hello"))  # Should return False