print("1 - ADDITION")
print("2 - SUBTRACTION")
print("3 - MULTIPICATION")
print("4 - DIVISION")
choose = int(input("Select a number :"))

if(choose in [1,2,3,4]) :
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))

    if(choose == 1) :
        result = n1 + n2
    elif(choose == 2) :
        result = n1 - n2  
    elif(choose == 3) :
        result = n1 * n2
    elif(choose == 4) :
        result = n1 // n2 

else :
    print("Invalid selection of numbers")

print("The result of the operation is {} ".format(result))
