# Exercise 2 - Product or sum

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
summary = num_1 + num_2
multiply = num_1 * num_2

if multiply < 1000:
    print(f"Product: {num_1} * {num_2} = {multiply}")
else:
    print(f"Sum: {num_1} * {num_2} = {summary}")