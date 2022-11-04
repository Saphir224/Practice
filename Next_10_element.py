#Write an algorithm that asks for a number and print the next 10 numbers
    
    
    #For version
first_number= float(input("Enter a number: "))
index_me=0
for index_me in range(10):
    index_me +=1 
    nombre_final= first_number + index_me
    print(nombre_final)

    #While version 
""" 
numberEnter = float(input("Enter a lot number those you want: "))
indexe_me = 1
while indexe_me<=10:
    final_num= numberEnter+indexe_me
    indexe_me+=1
    print(final_num) 
    
"""



