
#The addition's functionn
def addition_of_two (first_number, second_number):
    first_number= float
    second_number= float 
    return first_number + second_number

# The substraction's function
def substraction_of_two(first_number, second_number):
    first_number = float
    second_number = float
    return first_number - second_number

# The multiplication function
def multiplication_of_two (first_number, second_number):
    first_number =float
    second_number= float
    return first_number * second_number

#The division'funtion
def division_of_two (first_number, second_number) :
    first_number =float
    second_number = float
    second_number/= 0
    return first_number/second_number


# My calculator 
first_number= float(input("Enter the number: "))
seconde_number= float(input("Hit the second number: "))
operator=str(input("choise the operator between those (+,-,*,/): "))
 

if operator == "+" :
#Addition 
    print ("The addition of numbers is: " + str(addition_of_two(first_number,seconde_number)))

elif operator== "-":
# Substraction 
    print("The substraction of numbers is: " + str(substraction_of_two(first_number, seconde_number)))

elif operator== "*":
#Multiplication
    print("The multiplication of numbers is: " + str(multiplication_of_two(first_number, seconde_number)))

elif operator == "/":
#Divison 
    print("The division of numbers is: ") + str(division_of_two(first_number, seconde_number))
else:
    print("The operator you have inserted is not correct. Enter again: ")

 






