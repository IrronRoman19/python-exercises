def count_digits_in_number_into_loop(number):
    number = str(number)
    length = len(number)
    result = 0

    while result < length:
        result += 1

    return result

def main():
    print(count_digits_in_number_into_loop(int(input("Enter the multiply number: "))))

if __name__ == "__main__":
   main()