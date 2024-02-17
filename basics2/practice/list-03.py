numbers = [1, 2, 3, 4, 5, 6, 7]

def turn_numbers_into_square(numbers):
    square_numbers = []
    for i in numbers:
        square = i ** 2
        square_numbers.append(square)

    return square_numbers


def main():
    print(turn_numbers_into_square(numbers))

if __name__ == "__main__":
   main()