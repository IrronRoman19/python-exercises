def reverse_pyramid_pattern(num):
    for i in range(num, 0, -1):
        for j in range(i , 0, -1):
            print(f"{j}", end=" ")
        print("")

def main():
    reverse_pyramid_pattern(int(input("Enter the number: ")))

if __name__ == "__main__":
   main()