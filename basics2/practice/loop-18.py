def triangle_pattern(num):
    for i in range(1, num):
        for j in range(1, i):
            print("*", end=" ")
        print("")

    for i in range(num, 1, -1):
        for j in range(i , 1, -1):
            print("*", end=" ")
        print("")

def main():
    triangle_pattern(int(input("Enter the number: ")))

if __name__ == "__main__":
   main()