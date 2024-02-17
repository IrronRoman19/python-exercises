def calculate_cube_of_numbers(num):
    first_num = 1
    for i in range(first_num, num):
        cube = i * i * i
        print(f"Current Number is : {i}  and the cube is {cube}")

def main():
    calculate_cube_of_numbers(int(input("Enter the number: ")))

if __name__ == "__main__":
   main()