# Exercise 1 - Multiply list

num_list = [5, 12, 4, 23, 5]

result = 1

for i in num_list:
    print(f"Number: {i}, Multiply: {i * i}")
    result *= i
    

print(f"Result: {result}")