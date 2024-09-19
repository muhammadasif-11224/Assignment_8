num1 = float(input("enter your first number: "))
num2 = float(input("enter your second number: "))
print('press 1 for addition \n press 2 for subtraciton \n press 3 for multiplication \n press 4 for division ') 
choice = int(input('enter your choice from 1 to 4: '))
if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
    print('invalid number')