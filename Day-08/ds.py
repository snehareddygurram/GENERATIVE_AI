# -------------------------------
# DAY 4: DATA STRUCTURES IN PYTHON
# -------------------------------

# 1) ARRAY / LIST
# A list stores multiple values in one variable.
# In Python, we usually use "list" instead of saying "array".
nums = [10, 20, 30]

# Print the whole list
print("Array / List:", nums)

# Access the first item using index 0
print("First item in list:", nums[0])

# Add a new value at the end of the list
nums.append(40)

# Print updated list
print("Updated list:", nums)


# 2) STACK (LIFO = Last In First Out)
# Stack means the last item added is the first one removed.
# Example: stack of plates
stack = []

# Add items to stack
stack.append(1)
stack.append(2)
stack.append(3)

# Print current stack
print("Stack before pop:", stack)

# Remove the last item
removed_item = stack.pop()

# Print removed item
print("Removed from stack:", removed_item)

# Print stack after removing
print("Stack after pop:", stack)


# 3) QUEUE (FIFO = First In First Out)
# Queue means the first item added is the first one removed.
# Example: line at a store
from collections import deque

queue = deque()

# Add items to queue
queue.append("A")
queue.append("B")
queue.append("C")

# Print current queue
print("Queue before popleft:", list(queue))

# Remove the first item
first_removed = queue.popleft()

# Print removed item
print("Removed from queue:", first_removed)

# Print queue after removing
print("Queue after popleft:", list(queue))


# 4) DICTIONARY (KEY-VALUE PAIRS)
# Dictionary stores data as key-value pairs.
# Example: name -> Sneha, age -> 25
person = {
    "name": "Sneha",
    "age": 25
}

# Print whole dictionary
print("Dictionary:", person)

# Access value using key
print("Person name:", person["name"])

# Add a new key-value pair
person["city"] = "Richardson"

# Print updated dictionary
print("Updated dictionary:", person)

# Print all keys
print("Dictionary keys:", person.keys())

# Print all values
print("Dictionary values:", person.values())