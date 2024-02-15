list_1 = ["Hello", "I", "am", "Roman"]

def transform_from_list_to_join(list):
    joined_list = " ".join(list)
    return joined_list


def main():
    print(transform_from_list_to_join(list_1))

if __name__ == "__main__":
   main()