# Bitwise Operators
a = 10      # 1010 in binary
b = 7       # 0111 in binary

print("Bitwise Operators:")
print("a & b  =", a & b   )    # AND (1 only if both the inputs are 1)
print("a | b  =", a | b   )    # OR  (1 if one or more inputs is 1)
print("a ^ b  =", a ^ b   )    # XOR (1 if only one input is 1)
print("~a     =", ~a      )    # NOT
print("a << 1 =", a << 1  )    # Left shift  (a * 2**n)
print("a >> 1 =", a >> 1  )    # Right shift (a // 2**n)

# Logical Operators
x = True
y = False

print("\nLogical Operators:")
print("x and y =", x and y)
print("x or y  =", x or y) 
print("not x   =", not x)
