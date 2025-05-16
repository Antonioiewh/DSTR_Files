def floyd_modified_row():
    row = int(input("Please enter the row number:"))
    start = row * (row - 1) // 2 + 1
    print(start)
    numbers = []
    
    for i in range(row):
        num = (start + i) ** 2
        if row % 2 == 0:
            if num % 2 == 0:
                numbers.append(num)
        else:
            if num % 2 != 0:
                numbers.append(num)
    print(' * '.join(str(n) for n in numbers))
    print(f"The sum of row {row} is {sum(numbers)}")

floyd_modified_row()