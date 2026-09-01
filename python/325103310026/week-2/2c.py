start = int(input("enter start number:"))
end = int(input("enter end number:"))
total = 0

for i in range(start,end+1):
    if i % 2 == 0:
        total +=i
    
print("sum of even numbers between",start,"and",end,"is",total)