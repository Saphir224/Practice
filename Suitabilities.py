#Write an algorithm that asks the user for a number between 1 and 3 until the answer is correct
EnterNumbr= float(input("Enter a number between 1 and 3: "))
while (EnterNumbr > 3 or EnterNumbr < 1): 
    EnterNumbr=float(input("Enter again"))
print('The number is good')
