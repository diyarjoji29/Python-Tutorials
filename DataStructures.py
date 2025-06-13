print("......LIST......\n")

# Creating a list
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits)

# Accessing elements
print("fruits[1] : ",fruits[1])         # banana

# Modifying elements
fruits[1] = "blueberry"
print("\nAfter fruits[1] = 'blueberry' : ")
print(fruits)

# Adding
fruits.append("orange")
fruits.insert(1, "grape")
print("\nAfter fruits.append('orange')  & fruits.insert(1, 'grape') :")
print(fruits)

# Removing
fruits.remove("apple")   # removes first 'apple'
popped = fruits.pop()    # removes last element
print("\nAfter fruits.remove('apple')  &  fruits.pop() :")
print(fruits)
print("Popped : ",popped)

# Sorting and reversing
fruits.sort()
print("\nAfter sort :")
print(fruits)
fruits.reverse()
print("\nAfter reverse :")
print(fruits)

# Length
print("\nLength : ",len(fruits))

# Iterating
print("\nIterating")
for fruit in fruits:
    print(fruit)

# Membership
print("\n 'cherry' in fruits : ")
print("cherry" in fruits)



print("\n......TUPLE......\n")

# Creating a tuple
dimensions = (10, 20, 30, 10)
print(dimensions)

# Accessing elements
print("dimensions[1] : ", dimensions[1])  # 20

# Count and Index
print("\ndimensions.count(10) : ", dimensions.count(10))
print("dimensions.index(30) : ", dimensions.index(30))

# Length
print("\nLength : ", len(dimensions))

# Tuple unpacking
a, b, c, d = dimensions
print("\nUnpacked values : ", a, b, c, d)

# Iterating
print("\nIterating")
for val in dimensions:
    print(val)




print("\n\n......DICTIONARY......\n")

# Creating a dictionary
student = {"name": "Alice", "age": 21, "course": "CS"}
print(student)

# Accessing values
print("Name : ", student["name"])
print("Age using get : ", student.get("age"))

# Adding/Updating
student["grade"] = "A"
student["age"] = 22
print("\nAfter Adding/Updating :")
print(student)

# Removing
del student["course"]
removed = student.pop("grade")
print("\nAfter Removing 'course' and popping 'grade':")
print(student)
print("Removed grade : ", removed)

# Iterating
print("\nIterating")
for key in student:
    print(key, "->", student[key])

# Keys, Values, Items
print("\nKeys : ", student.keys())
print("Values : ", student.values())
print("Items : ", student.items())

# Membership
print("\n'name' in student : ", "name" in student)

# Copy
copy_student = student.copy()
print("\nCopy of student : ", copy_student)



print("\n\n......SET......\n")

# Creating a set
colors = {"red", "green", "blue", "red"}
print(colors)

# Adding
colors.add("yellow")
print("\nAfter adding 'yellow' : ", colors)

# Removing
colors.remove("red")
colors.discard("pink")  # No error if not found
print("\nAfter remove 'red' and discard 'pink' : ", colors)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("\na = ", a)
print("b = ", b)

print("\nUnion : ", a.union(b))
print("Intersection : ", a.intersection(b))
print("Difference (a - b) : ", a.difference(b))
print("Symmetric Difference : ", a.symmetric_difference(b))

# Membership
print("\n'green' in colors : ", "green" in colors)

# Iterating
print("\nIterating")
for color in colors:
    print(color)
