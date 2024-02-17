def find_the_factorial(num):

    if num[-1] == "!":
        num = int(num[:-1])
        factorial = 1
        for i in range(num, factorial, -1):
            factorial = factorial *i

        return factorial
    else:
        return "Invalid error!"
    

def main():
    print(find_the_factorial(input("Enter the number: ")))

if __name__ == "__main__":
   main()