def sum_the_series(num):
    first_num = 1
    seria = "2"
    res = 0
    for i in range(first_num, (num + 1)):
        int_seria = seria * i
        int_seria = int(int_seria)
        res += int_seria

    return res

def main():
    print(sum_the_series(int(input("Enter the number: "))))

if __name__ == "__main__":
   main()