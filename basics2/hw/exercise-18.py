def comparing_three_numbers(num_1, num_2, num_3):
    result = 0
    if num_1 == num_2 == num_3:
        result = num_1 + num_2 + num_3
        return f"Sum of three numbers: {result}"
    else:
        return "The numbers are not equal each other"

def main():
    num_1 = int(input("Enter 1st number: "))
    num_2 = int(input("Enter 2nd number: "))
    num_3 = int(input("Enter 3rd number: "))
    print(comparing_three_numbers(num_1, num_2, num_3))

if __name__ == "__main__":
   main()