list_1 = [10, 20, 30, 40, 50]

def reverse_display_of_list_with_loop(list_1):
    for i in list_1[::-1]:
        print(i)

def main():
    reverse_display_of_list_with_loop(list_1)

if __name__ == "__main__":
   main()