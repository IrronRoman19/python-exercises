# Exercise 2 - find the largest number in a list without max()

list_1 = [5, 10, 60, 9, 12, 53, 120, 53, 12, 64]

max_result = 0

for i in list_1:
    if i > max_result:
        max_result = i
    else:
        pass

print(f"Largest number in a list: {max_result}")