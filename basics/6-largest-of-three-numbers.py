# Exercise 6 - Largest of three numbers

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if num_1 > num_2:
    if num_1 > num_3:
        print(f"1st number: {num_1}")
    else:
        print(f"3rd number: {num_3}")

elif num_1 < num_2:
    if num_3 < num_2:
        print(f"2nd number: {num_2}")
    else:
        print(f"3rd number: {num_3}")