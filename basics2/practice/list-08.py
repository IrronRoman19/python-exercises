list_1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

def extend_list_by_adding_sublist(list_1, sub_list):
    list_2 = list_1[2]
    list_3 = list_2[1]
    list_4 = list_3[2]

    for i in sub_list:
        list_4.append(i)

    return list_1


def main():
    print(extend_list_by_adding_sublist(list_1, sub_list))

if __name__ == "__main__":
   main()