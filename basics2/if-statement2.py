# If Statement

num = int(input("Enter the number: "))

if (num % 5 == 0) and (num % 7 == 0) and (1500 <= num <= 2700):
    print(f"Yes! is number {num}")
else:
    if not(num % 5 == 0):
        print(f"No! {num} is not divided by 5")
    if not(num % 7 == 0):
        print(f"No! {num} is not divided by 7")
    if not(1500 <= num <= 2700):
        print(f"No! {num} is not in ranges between 1500 to 2700")