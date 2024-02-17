list_1 = ["M", "na", "i", "Ke"]
list_2 = ["y", "me", "s", "lly"]

def join_two_indexes(list_1, list_2):
    total_list = []
    index = 0
    last_index_1 = len(list_1) - 1
    last_index_2 = len(list_2) - 1
    while (index <= last_index_1) and (index <= last_index_2):
        united_word = []
        united_word.append(list_1[index])
        united_word.append(list_2[index])
        united_word = "".join(united_word)
        index += 1
        total_list.append(united_word)

    return total_list

def main():
    print(join_two_indexes(list_1, list_2))

if __name__ == "__main__":
   main()