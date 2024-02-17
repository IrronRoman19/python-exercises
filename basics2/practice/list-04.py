list_1 = ["Hello ", "take "]
list_2 = ["Dear", "Sir"]

def concetate_two_lists(list_1, list_2):

    total_list = []

    for i in list_1:
        for j in list_2:
            concetration_list = []
            concetration_list.append(i)
            concetration_list.append(j)
            concetration_list = "".join(concetration_list)
            total_list.append(concetration_list)

    return total_list

def main():
    print(concetate_two_lists(list_1, list_2))

if __name__ == "__main__":
   main()