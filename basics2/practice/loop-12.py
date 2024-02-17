num_1 = 0
num_2 = 1
rang = 10

def display_fibonacci(num_1, num_2, rang):
    res = 0
    count = 0
    print("Fibonacci sequence:")
    while count < rang:
        print(res, end=" ")
        count += 1
        num_1 = num_2
        num_2 = res 
        res = num_1 + num_2
    

def main():
    display_fibonacci(num_1, num_2, rang)

if __name__ == "__main__":
   main()