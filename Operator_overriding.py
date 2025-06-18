class addition:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val + 3

class subtraction:
    def __init__(self, val):
        self.val = val

    def __sub__(self, other):
        return self.val - other.val - 3

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

obj1 = addition(a)
obj2 = addition(b)
print("Custom addition:", obj1 + obj2)  

obj3 = subtraction(a)
obj4 = subtraction(b)
print("Custom subtraction:", obj3 - obj4) 
