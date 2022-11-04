""" Write an algorithm that asks the user for a number between 10 and 20 until
    the answer is correct. If the  number that you have entered is smaller than 10
    print"Bigger". With number bigger than 20 write "Smaller". """
    
numberEntered= float(input("Enter the number between 10 and 20: "))
while numberEntered<10 or numberEntered>20:
    if numberEntered<10:
        numberEntered=float(input("Write a number that bigger than your last number"))
    elif numberEntered > 20:
        numberEntered=float(input("Write a number that smaller than your last number"))
print("Good job")
