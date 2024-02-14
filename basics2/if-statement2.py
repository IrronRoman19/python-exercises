# If Statement

num = int(input("Enter the number: "))

# Option 1

if (num % 5 == 0) and (num % 7 == 0) and (1500 <= num <= 2700):
    print(f"Yes! is number {num}")
else:
    if not(num % 5 == 0):
        print(f"No! {num} is not divided by 5")
    if not(num % 7 == 0):
        print(f"No! {num} is not divided by 7")
    if not(1500 <= num <= 2700):
        print(f"No! {num} is not in ranges between 1500 to 2700")

# Option 2

# if (num % 35 == 0) and (1500 <= num <= 2700):
#     print(f"Yes! is number {num}")
# else:
#     if not(num % 35 == 0):
#         print(f"No! {num} is not divided by 35")
#     if not(1500 <= num <= 2700):
#         print(f"No! {num} is not in ranges between 1500 to 2700")