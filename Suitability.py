#Write an algorithm that asks the user for a number between 1 and 3 until the answer is correct
EnterNumber= float(input("Enter a number between 1 and 3: "))
while  1 > EnterNumber or EnterNumber > 3 : 
    print("The number you have selected is not correct")
    EnterNumber = float(input("Enter again a number"))
    if 1<= EnterNumber and EnterNumber <= 3: 
        print("The number is good")
        break
print("Good Job")