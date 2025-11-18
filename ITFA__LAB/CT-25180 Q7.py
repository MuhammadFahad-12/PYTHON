a = int(input("Enter three numbers: "))
b = int(input())
c = int(input())

if a < b and a < c:
    print("a is smallest: ", a)
elif b < c and b < a:
    print("b is smallest", b)
else:
    print("c is smallest", c)