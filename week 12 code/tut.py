# Qn1
# Memory Address = Start Address + (Index × Bytes Per Element)
# Start Address: The memory address where the array begins (e.g., 2146).
# Index: The position of the element in the array (e.g., 4 for 'L').
# Bytes Per Element: The size of each element in bytes (e.g., 2 bytes for each character).
# For index 4, start address 2146, and 2 bytes per element:
# Memory Address = 2146 + (4 × 2) = 2146 + 8 = 2154


def get_memory_address(start_address, index, bytes_per_element):
    """
    Computes the memory address of a specific cell in an array.

    Parameters:
        start_address (int): The memory address where the array starts.
        index (int): The index of the desired element in the array.
        bytes_per_element (int): The number of bytes each element occupies.

    Returns:
        int: The memory address of the element at the given index.
    """
    return start_address + (index * bytes_per_element)

# Example usage:
if __name__ == "__main__":
    start_address = 2146
    bytes_per_element = 2
    index = 4  # For the character 'L' in "SAMPLE"
    address = get_memory_address(start_address, index, bytes_per_element)
    print(f"Memory address of index {index}: {address}")



# Qn2

import array

# a) Create an array of integers, array_int
array_int = array.array('i')
print("a) Created array:", array_int.tolist())

# b) Initialise array_int with the following values [1, 5, 7, 9, 100]
array_int = array.array('i', [1, 5, 7, 9, 100])
print("b) Initialised array:", array_int.tolist())

# c) Insert the number 3 into the second element of array_int
array_int.insert(1, 3)
print("c) After inserting 3 at index 1:", array_int.tolist())

# d) Remove the number 100 from array_int
array_int.remove(100)
print("d) After removing 100:", array_int.tolist())

# e) Append the number 11 into array_int
array_int.append(11)
print("e) After appending 11:", array_int.tolist())

# f) Reverse the order of the numbers in array_int
array_int.reverse()
print("f) After reversing:", array_int.tolist())


# Qn3
# 
# a) temp = primes[3:6]
#    - This creates a new list 'temp' with references to the same integer objects as primes[3], primes[4], primes[5].
#    - primes: [2] [3] [5] [7] [11] [13] [17] [19]
#               0   1   2   3    4    5    6    7
#    - temp:   [7] [11] [13]
#               0   1    2
#    - Both lists reference the same integer objects for 7, 11, 13.
#
# b) temp[2] = 15
#    - This changes temp[2] to reference a new integer object 15.
#    - primes is NOT affected; primes[5] still references 13.
#    - primes: [2] [3] [5] [7] [11] [13] [17] [19]
#               0   1   2   3    4    5    6    7
#    - temp:   [7] [11] [15]
#               0   1    2
#
# c) counters = [0] * 8
#    - This creates a list of 8 elements, all referencing the same integer object 0.
#    - counters: [0] [0] [0] [0] [0] [0] [0] [0]
#                 |   |   |   |   |   |   |   |
#                 +---+---+---+---+---+---+---+
#                       (same 0 object)
#
# d) counters[2] += 1
#    - This is equivalent to counters[2] = counters[2] + 1.
#    - counters[2] now references a new integer object 1.
#    - The other elements still reference the original 0 object.
#    - counters: [0] [0] [1] [0] [0] [0] [0] [0]
#                 |   |   |   |   |   |   |   |
#                 +---+   +---+---+---+---+---+
#                     |       (same 0 object)
#                 (new 1 object)
# filepath: c:\Users\nghwe\OneDrive\schhol\Y2S1\DATASTRUCALGO\week 12 code\tut.py
# Qn3
# 
# a) temp = primes[3:6]
#    - This creates a new list 'temp' with references to the same integer objects as primes[3], primes[4], primes[5].
#    - primes: [2] [3] [5] [7] [11] [13] [17] [19]
#               0   1   2   3    4    5    6    7
#    - temp:   [7] [11] [13]
#               0   1    2
#    - Both lists reference the same integer objects for 7, 11, 13.
#
# b) temp[2] = 15
#    - This changes temp[2] to reference a new integer object 15.
#    - primes is NOT affected; primes[5] still references 13.
#    - primes: [2] [3] [5] [7] [11] [13] [17] [19]
#               0   1   2   3    4    5    6    7
#    - temp:   [7] [11] [15]
#               0   1    2
#
# c) counters = [0] * 8
#    - This creates a list of 8 elements, all referencing the same integer object 0.
#    - counters: [0] [0] [0] [0] [0] [0] [0] [0]
#                 |   |   |   |   |   |   |   |
#                 +---+---+---+---+---+---+---+
#                       (same 0 object)
#
# d) counters[2] += 1
#    - This is equivalent to counters[2] = counters[2] + 1.
#    - counters[2] now references a new integer object 1.
#    - The other elements still reference the original 0 object.
#    - counters: [0] [0] [1] [0] [0] [0] [0] [0]
#                 |   |   |   |   |   |   |   |
#                 +---+   +---+---+---+---+---+
#                     |       (same 0 object)
#                 (new