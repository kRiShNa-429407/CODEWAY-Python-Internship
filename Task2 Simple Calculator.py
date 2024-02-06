## Input the two numbers from the user

n1=float(input("Enter the  first number:\n"))
n2=float(input("Enter the second number:\n"))

## Now take the choice of user to perform basic arithmetic operations

choice=int(input("Press 1 for Addition:\nPress 2 for Subtraction:\nPress 3 for Multiplication:\nPress 4 for Division\n"))

## Note : \n is an escape sequence which is used to print the statement in a new line.

## Use match-case to print take the choice and print desired output

match(choice):
    case 1:
        print("The Addition of two numbers",n1,"and",n2,"is",n1+n2)
    case 2:
        print("The Subtraction of two numbers", n1, "and", n2, "is", n1 - n2)
    case 3:
        print("The Multiplication of two numbers", n1, "and", n2, "is", n1 * n2)
    case 4:
        print("The Division of two numbers", n1, "and", n2, "is", n1 / n2)
    case _:
        print("Invalid Choice ")

## Note : last case i.e "case _" is a default case which is run if user choice is invalid



