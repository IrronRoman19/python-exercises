def pyramid_pattern(num):
    for i in range(1, (num + 1)):
        for j in range(1, (i + 1)):
            print(f"{j}", end=" ")
        print("")



def main():
    pyramid_pattern(int(input("Enter the number: ")))

if __name__ == "__main__":
   main()