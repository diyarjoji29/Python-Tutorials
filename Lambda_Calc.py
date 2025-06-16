students =  [("Alice", 88), ("Bob", 72), ("Charlie", 95), ("David", 85)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

#.......CALCULATOR........

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

print("CALCULATOR")
num1=int(input("Enter two numbers :\n"))
num2=int(input())

print("1.Addition\t2.Subtraction\t3.Multiplication\t4.Division\t5.Modulus")
print("Please enter your choice: ")
choice=int(input())
if choice==1:
    print("Sum= ",add(num1,num2))
elif choice==2:
    print("Difference= ",sub(num1,num2))
elif choice==3:
    print("Product= ",mult(num1,num2))
elif choice==4:
    print("Quotient= ",div(num1,num2))
elif choice==5:
    print("Modulus= ",mod(num1,num2))

