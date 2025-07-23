import pancake as stack

print("POSTFIX EVAL")

while True:
    tokens = input("Enter a postfix expression: ")
    print("You entered:", tokens)
    
    tokens_split = tokens.split(" ")
    print("Split tokens:", tokens_split)

    #Create a stack
    teststack = stack.pancake()
    
    #Quit
    if tokens_split[0] == "E":
        print("Exiting input loop.")
        break
    else:
        valid = True
        while len(tokens_split) > 0:
            

            
            item = tokens_split.pop(0)
            print("Current item:", item)
            if item.isdigit():
                teststack.push(int(item))
            elif item == "+":
                print("Adding")
                if len(teststack) >1:
                    teststack.push(teststack.pop() + teststack.pop())
                else:
                    valid = False 
                    print("GG")
                    break
            elif item == "-":
                print("Subtracting")
                if len(teststack) > 1:
                    num2 = teststack.pop()
                    num1 = teststack.pop()
                    teststack.push(num1 - num2)
                else:
                    valid = False 
                    print("GG")
                    break
            elif item == "*":
                print("Multiplying")
                if len(teststack) > 1:
                    
                    teststack.push(teststack.pop() * teststack.pop())
                else:
                    valid = False 
                    print("GG")
                    break
            elif item == "/":
                print("Dividing")
                if len(teststack) > 1:
                    num2 = teststack.pop()
                    num1 = teststack.pop()
                    teststack.push(num1 / num2)
                else:
                    valid = False 
                    print("GG")
                    break
                
#Testcases
# 10 5 / = 2
# 10 5 * = 5
# 10 5 + = 15 
# 10 2 ^ = 100
# 10 5 - = 5