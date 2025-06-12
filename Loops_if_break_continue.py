#if / if-elif / if-elif-else
num=int(input("Enter a number : "))
if num>10:
    print("Greater than 10")
elif num<10:
    print("Less than 10")
else:
    print("It is 10")

#while loop
sum=0
num1=num
while num1!=0:
    d=num1%10
    num1=num1//10
    sum+=d
print("Sum of digits of ",num," : ",sum)


#Using break and continue
i=-6
while True:
    i+=1
    if(i==0):
        print("  ",end="")
        continue
    elif(i>5):
        break
    print("  ",i,end="")
        
print()


#for loop
print("18's multiplication table: ")
for i in range (10):
    print("18 x ",i," = ",(i*18))

print("Cars: ")
cars=["Hyundai","Tesla","Mahindra","Suzuki"]
for c in cars:
    print(c)


print("2 to 10 (incremented by 2)")
for i in range(2,10,2):   # 2 to 10 (incremented by 2)
    print(' ',i,end="")
print()
print("10 to 2 (decremented by 2)")
for i in range(10, 2, -2):  # 10 to 2 (decremented by 2)
    print(' ',i,end="")
print()

person = {"name": "Alice", "age": 25, "city": "Delhi"}
for key, value in person.items():
    print(key, ":", value)

for _ in range(5): # when we do not need a variable in body
    print("Hello")
