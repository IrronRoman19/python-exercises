list_1 = [10, 20, 30, 40]
list_2 = [100, 200, 300, 400]

def iterate_lists(list_1, list_2):
    iterate_list = []
    index = 0

    list_2 = list_2[::-1]

    last_index_1 = len(list_1) - 1
    last_index_2 = len(list_2) - 1
    while (index <= last_index_1) and (index <= last_index_2):
        united_lists = []
        united_lists.append(list_1[index])
        united_lists.append(list_2[index])
        index += 1
        iterate_list.append(united_lists)

    for i in iterate_list:
        print(f"{i[0]} {i[1]}")


def main():
    iterate_lists(list_1, list_2)

if __name__ == "__main__":
   main()