def calculate_sum_number(num):
    res = 0
    for i in range(num + 1):
        res += i

    return res

def main():
    print(calculate_sum_number(int(input("Enter the sum number: "))))

if __name__ == "__main__":
   main()