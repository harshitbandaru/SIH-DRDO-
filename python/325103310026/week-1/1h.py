# Swapping of two numbers without using a temporary variable 

x = float(input("Please enter a value for x = "))
y = float(input("Please enter a value for y = "))

x = x + y
y = x - y
x = x - y

print("x is :", x )
print("y is :", y )

