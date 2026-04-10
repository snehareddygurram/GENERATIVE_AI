#variables
name = "sneha"
age = "29"
height = 5.0
print("Name", name)
print("Age", age)
print("Height", height)

#Data types
weight = 63.10
is_fit = True
print(type(name))
print(type(age))
print(type(height))
print(type(weight))
print(type(is_fit))

#lists
numbers = [10, 20, 30, 40, 50]
print("Frist number:", numbers[0])
numbers.append(60)
print("Updated List:", numbers)

for num in numbers:
    print("List Item:", num)

print("Sum of list:", sum(numbers))  

# Dictionary
person = {
    "name": "Sneha",
    "age": 25,
    "city": "Richardson"
}
print("Person name:", person["name"])

person["job"] = "GenAI Learner"
print("Upadted dictionary:", person)

#Loops
for i in range(5):
    print("For loop:", i)
i = 0
while i < 3:
    print("While loop:", i)
    i += 1

#Functions
def greet(name):
    return "hello" + name
print(greet("Sneha"))

def square(x):
    return x * x
print("Square of 5:", square(5))

#Even or Odd
num = 10
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is odd")























































































































