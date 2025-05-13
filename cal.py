# Program for calculator.

def cal():
    # Ask the user if they want to use the calculator.
    a = input('Do you want to use the calculator? (Y/N): ').upper()

    # Repeat the operation while the user chooses 'Y'.
    while a == 'Y':
        try :
            # Take two numeric inputs from the user.
            n1 = int(input('Enter a number : '))
            n2 = int(input('Enter another number : '))

            # Ask the user to choose the operation.
            s = int(input('Choose an operation : (1 = Sum, 2 = Subtract, 3 = Multiply, 4 = Divide) : '))
            
            # Perform the selected operation.
            if s == 1 :
                print(f'The result of {n1} + {n2} is : {n1+n2}')
            elif s == 2 :
                print(f'The result of {n1} - {n2} is : {n1-n2}')
            elif s == 3 :
                print(f'The result of {n1} * {n2} is : {n1*n2}')
            elif s == 4 :
                if n2 == 0 :
                    print('Division by Zero is not defined')
                else :
                    print(f'The result of {n1} / {n2} is : {n1/n2}')
        except:
            print('Please enter correct number')
        
        # Ask the user if they want to perform another calculation.
        a = input('Do you want to use the calculator again? (Y/N) : ').upper()

    #Close the program.
    print('Thank you for using the calculator!')

cal()
