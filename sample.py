a = int(input("Enter any Number: "))
b = int(input("Enter any Number: "))
c = int(input("Enter any Number: "))

if a>b and a>c:
    print(a," is Greater than ",b," and ",c)
elif b>a and b>c:
    print(b," is Greater than ",a," and ",c)
else:
    print(c,"is Greater than ",a," and ",b)        