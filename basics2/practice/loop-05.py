numbers = [12, 75, 150, 180, 145, 525, 50]

def display_numbers_with_loop(numbers):
    for i in numbers:
        if (i % 5 == 0) and i <= 150:
            print(i)
        elif i > 500:
            break
        else:
            continue

def main():
    display_numbers_with_loop(numbers)

if __name__ == "__main__":
   main()