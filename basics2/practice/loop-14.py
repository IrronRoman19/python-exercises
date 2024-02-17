def reverse_integer_number(num):
    num = str(num)
    reverse = []
    for i in num[::-1]:
        reverse.append(i)

    reverse = "".join(reverse)
    return reverse

def main():
    print(reverse_integer_number(int(input("Enter the number: "))))

if __name__ == "__main__":
   main()