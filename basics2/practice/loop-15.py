my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def display_odd_positions(my_list):
    for i in my_list[1::2]:
        print(f"{i}", end=" ")


def main():
    display_odd_positions(my_list)

if __name__ == "__main__":
   main()