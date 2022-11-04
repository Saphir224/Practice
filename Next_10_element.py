#Write an algorithm that asks for a number and print the next 10 numbers

first_number= float(input("Enter a number: "))
index_me=0
for index_me in range(10):
    index_me +=1 
    nombre_final= first_number + index_me
    print(nombre_final)



