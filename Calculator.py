#Start a loop and ask for input on what kind of operation to perform
B = True
while B:
    operation = input("Do you want to add (+), subtract (-), multiply (*), or divide (/)?\n")
    #Check if the input is a valid operation symbol and execute. If not restart the loop.
    if operation == '+': 
        #Take the two numbers as input for the operation, add them, and print the answer
        x = input("Enter your first number:\n")
        y = input("Enter your second number:\n")
        ans = int(x) + int(y)
        print("The addition of your numbers is " + str(ans))
        #Ask if user wants to restart or quit out
        restart = input("Do you want to restart? (y/n)\n")
        if restart != 'y':
            B = False
            
    elif operation == '-': 
        #Take the two numbers as input for the operation, subtract them, and print the answer
        x = input("Enter your first number:\n")
        y = input("Enter your second number:\n")
        ans = int(x) - int(y)
        print("The subtraction of your numbers is " + str(ans))
        #Ask if user wants to restart or quit out
        restart = input("Do you want to restart? (y/n)\n")
        if restart != 'y':
            B = False
            
    elif operation == '*': 
        #Take the two numbers as input for the operation, multiply them, and print the answer
        x = input("Enter your first number:\n")
        y = input("Enter your second number:\n")
        ans = int(x) * int(y)
        print("The multiplication of your numbers is " + str(ans))
        #Ask if user wants to restart or quit out
        restart = input("Do you want to restart? (y/n)\n")
        if restart != 'y':
            B = False
            
    elif operation == '/':
        #Take the two numbers as input for the operation, divide them, and print the answer
        x = input("Enter your first number:\n")
        y = input("Enter your second number:\n")
        ans = float(x) / float(y)
        print("The division of your numbers is " + str(ans))
        #Ask if user wants to restart or quit out
        restart = input("Do you want to restart? (y/n)\n")
        if restart != 'y':
            B = False
        
    else:
        print("Not valid input.")