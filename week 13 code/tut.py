# Topic 08: Stacks
#
# 1. Transform the following infix expressions to postfix and prefix:
#
#    a. (A * B) / C
#       - Postfix: A B * C /
#       - Prefix:  / * A B C
#
#    b. A – (B * C) + D / E
#       - Postfix: A B C * - D E / +
#       - Prefix:  + - A * B C / D E
#
#    c. (X – 5) + (7 * Z) / V
#       - Postfix: X 5 - 7 Z * V / +
#       - Prefix:  + - X 5 / * 7 Z V
#
#    d. V * W * 8 + Y – Z
#       - Postfix: V W * 8 * Y + Z -
#       - Prefix:  - + * V W 8 Y Z
#
#    e. A / B * C – D + E
#       - Postfix: A B / C * D - E +
#       - Prefix:  + - * / A B C D E
#
# Explanation:
# - Infix: Operators are written between operands (e.g., A + B).
# - Postfix: Operators are written after operands (e.g., A B +).
# - Prefix: Operators are written before operands (e.g., + A B).
# - Conversion uses operator precedence and parentheses to determine order.
#
# 2. Trace and evaluate the following postfix expressions:
#
#    a. [3 8 + ][10 3 -][ * ]
#       Step 1: 3 8 + = 11
#       Step 2: 10 3 - = 7
#       Step 3: 11 7 * = 77
#       Result: 77
#   My intepretation:
#   3 8 + = 3 + 8 = 11 ( read left to right)
#   10 3 - = 10 - 3 = 7
#   11 7 * = 11 * 7 = 77
#
#    b. 2 3 ^ 4 ^
#       Step 1: 2 3 ^ = 8
#       Step 2: 8 4 ^ = 4096
#       Result: 4096
#
#    c. 8 2 + 10 - 10
#       Step 1: 8 2 + = 10
#       Step 2: 10 10 - = 0
#       Result: 0
#
#    d. 15 3 / 5 10 - / 100 ^
#       Step 1: 15 3 / = 5
#       Step 2: 5 10 - = -5
#       Step 3: 5 / -5 = -1
#       Step 4: -1 100 ^ = 1
#       Result: 1
#
#    e. 25 4 * 20 15 - / 2 / 18 +
#       Step 1: 25 4 * = 100
#       Step 2: 20 15 - = 5
#       Step 3: 100 5 / = 20
#       Step 4: 20 2 / = 10
#       Step 5: 10 18 + = 28
#       Result: 28
#
# Explanation:
# - Postfix evaluation uses a stack:
#   1. Push operands onto the stack.
#   2. When an operator is encountered, pop required operands, apply the operator, and push the result back.
#   3. Continue until the end; the final value on the stack
# 3. Write a Python function – transfer(S, T) with no more than 3 lines of code,
#    that transfers all elements from stack S to stack T, so that the element at the top of S
#    is the first to be inserted onto T, and the element at the bottom of S ends up at the top or T.

def transfer(S, T):
    while S:
        T.append(S.pop())

# Explanation:
# - This function pops elements from S and pushes them onto T.
# - The top of S becomes the top of T, reversing the order.

# 4. Write a recursive Python function – recEmptyStack(S) for removing all the elements from a stack S.

def recEmptyStack(S):
    if S:
        S.pop()
        recEmptyStack(S)

# Explanation:
# - The function pops one element and calls itself recursively until the stack is empty.
# - This removes all elements from S using recursion.

