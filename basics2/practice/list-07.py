list_1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def adding_item_to_list(list_1):
    list_2 = list_1[2]
    list_3 = list_2[2]
    list_3.append(7000)

    return list_1

def main():
    print(adding_item_to_list(list_1))

if __name__ == "__main__":
   main()