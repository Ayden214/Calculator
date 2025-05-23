#Start a loop and ask for input, check if input is valid, and ask if the loop should end
B = True
while B:
    #Make boolean to check if operations need to be skipped
    good = True
    #Take in two numbers and the operator as input and print answer
    x = input("Enter your first number:\n")
    #This checks if the first input is a valid number, if not, skip to end
    try:
        type(int(x))
    except:
        print("Not valid input.")
        good = False
        
    if good:    
        operator = input("Do you want to add (+), subtract (-), multiply (*), or divide (/)?\n")
        #This checks if the second input is an operator
        if(operator != '+' and operator != '-' and operator != '/' and operator != '*'):
            print("Not valid input")
            good = False
    
    if good:    
        y = input("Enter your second number:\n")
        #This checks if the third input is a valid number, if not, skip to end
        try:
            type(int(y))
        except:
            print("Not valid input.")
            good = False
        
    if good:    
        #this performs the operation based on the inputs
        if operator == '+': 
            ans = int(x) + int(y)
            
        elif operator == '-': 
            ans = int(x) - int(y)
                
        elif operator == '*':
            ans = int(x) * int(y)
                
        elif operator == '/':
            ans = float(x) / float(y)
            
        try:
            print("Your answer is: " + str(ans))
        except:
            print("Error.") 
        
    restart = input("Do you want to restart? (y/n)\n")
    if restart != 'y':
       B = False