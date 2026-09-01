def QUAQE(a,b,c,x):
    quadratic_value=a*x*x+b*x+c
    discriminant=b*b-4*a*c
    sum_roots=-b/a
    product_roots=c/a

    return quadratic_value,discriminant,sum_roots,product_roots

q,d,s,p=QUAQE(1,-5,6,3)

print("quadratic value:", q)
print("discriminant:",d)
print("sum of roots:",s)
print("product of roots:",p)