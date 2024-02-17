num_1 = 25
num_2 = 50

def display_prime_number_in_range(num_1, num_2):
    for i in range(num_1, (num_2 + 1)):
        if i > 1:
            for j in range(2, int(i / 2) + 1):
                if i % j == 0:
                    break
            else:
                print(i)
        else:
            break


def main():
    display_prime_number_in_range(num_1, num_2)

if __name__ == "__main__":
   main()