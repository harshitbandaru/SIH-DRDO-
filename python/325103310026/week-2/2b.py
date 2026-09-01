# To write a program to find the largest number among the given numbers (multi-way if-elif-else statements)

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:" ))
if a >= b and a >= c:
    print("the largest number is:",a)

elif b >= a and b >= c:
    print("the largest number is:",b)

else:
    print("the largest number is:",c)
    
   