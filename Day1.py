num1=10
num2=20
sum=num1+num2
print("sum",sum)

for j in range(5):
    for i in range (j):
        print("*",end="")
    print("\n")


for i in range(5,-1,-1):
    for j in range (i):
        print("*",end="")
    print("\n")


def gcd(a,b):
    while(b!=0):
        c=a%b
        a=b
        b=c
    print("GCD=",a)
    return


a=int(input("Enter 2 numbers\n"))
b=int(input())
gcd(a,b)
