def probability_set_on():
    input_odd_num = str(input('(Hint1) Enter the number of odd numbers (s): '))
    input_one_digit = str(input('(Hint2) Enter any number of digit (0 - 9): '))
    total_guess_pool = 10*10*10
    total_valid_pool1 = 0
    total_valid_pool2 = 0
    flag = False
    #go through pool of guesses
    for i in range(999):
        guess_num = f'{i:03}'
        #check hint 1 first0
        #This variable
        odd_num = 0
        for x in guess_num:
            x = int(x)
            if (x%2 !=0):
                odd_num +=1
        if odd_num == int(input_odd_num):
            total_valid_pool1 +=1
        if odd_num == int(input_odd_num) and input_one_digit in guess_num:
            total_valid_pool2 +=1




    print(f'(a)\n Prob of numbers fufilling hint 1: {(total_valid_pool1 / total_guess_pool)*100}')
    print(f'(b)\n Prob of numbers fulfil both hints: {(total_valid_pool2/total_guess_pool)*100}')




probability_set_on()