# Exercise 6 - Largest of three numbers

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

if (num_1 > num_2 and num_1 > num_3):
    print(f"1st number {num_1} is greatest")
elif (num_1 < num_2 and num_3 < num_2):
    print(f"2nd number {num_2} is greatest")
elif (num_1 > num_2 and num_1 < num_3) or (num_1 < num_2 and num_3 > num_2) or (num_1 == num_2 and num_3 > num_2):
    print(f"3rd number {num_3} is greatest")
elif (num_1 == num_2 and num_1 > num_3) and (num_1 == num_2 and num_2 > num_3):
    print(f"1st number {num_1} and 2rd number {num_2} are greatest")
elif (num_1 > num_2 and num_1 == num_3) and (num_3 > num_2 and num_1 == num_3):
    print(f"1st number {num_1} and 3rd number {num_3} are greatest")
elif (num_1 < num_2 and num_3 == num_2) and (num_1 < num_3 and num_3 == num_2):
    print(f"2nd number {num_2} and 3rd number {num_3} are greatest")
elif (num_1 == num_2 and num_1 == num_3 and num_2 == num_3):
    print(f"1st number {num_1}, 2rd number {num_2} and 3rd number {num_3} are greatest")

# Old solution

# if num_1 > num_2:
#     if num_1 > num_3:
#         print(f"1st number {num_1} is greatest")
#     elif num_1 < num_3:
#         print(f"3rd number {num_3} is greatest")
#     elif num_1 == num_3:
#         print(f"1st number {num_1} and 3rd number {num_3} are greatest")

# elif num_1 < num_2:
#     if num_3 < num_2:
#         print(f"2nd number {num_2} is greatest")
#     elif num_3 > num_2:
#         print(f"3rd number {num_3} is greatest")
#     elif num_3 == num_2:
#         print(f"2nd number {num_2} and 3rd number {num_3} are greatest")

# elif num_1 == num_2 and num_1 == num_3 and num_2 == num_3:
#     print(f"1st number {num_1}, 2rd number {num_2} and 3rd number {num_3} are greatest")
# elif num_1 == num_2:
#     print(f"1st number {num_1} and 2rd number {num_2} are greatest")