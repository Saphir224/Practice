# Write a algorithm that ask a user to enter a number then print the multiplication table

number_enter=float(input("Enter the number you want for multiplication table: "))
print("Table of " + str(number_enter) + " : " )
for indexe_me in range(10):
    indexe_me+=1
    print(str(number_enter)+ " * "+ str(indexe_me)+ " = "+ str(number_enter*indexe_me))