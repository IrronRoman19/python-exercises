color_list = ["Red","Green","White","Black"]

def taking_first_and_last_from_list(list):
    return f"First color in list: {list[0]}\nLast color in list: {list[-1]}"

def main():
    print(taking_first_and_last_from_list(color_list))

if __name__ == "__main__":
   main()