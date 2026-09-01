S =["AUDI","BMW","PORSCHE","PAGANI","FERRARI","LAMBORGHINI","MASERATI","ROLLS ROYCE","BMW"]

# Append
S.append("MCLAREN")
print(S)

# Count
Y= S.count("BMW")
A= S.count("PAGANI")
print(Y)
print(A)

# Index
T= S.index("FERRARI")
print(T)

T = S.index("BMW")
print(T)

# Remove
S.remove("BMW")
print(S)

# Sort
S.sort()
print(S)

# Pop
H= S.pop(2)
print(H)
print(S)

# Reverse
S.reverse()
print(S)
