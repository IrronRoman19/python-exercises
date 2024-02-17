num_1 = 1
num_2 = 10

def multiplication_of_numbers(num, num_1, num_2):
    for i in range(num_1, (num_2 + 1)):
        multiply = i * num
        print(multiply)

def main():
    multiplication_of_numbers(int(input("Enter the multiply number: ")), num_1, num_2)

if __name__ == "__main__":
   main()