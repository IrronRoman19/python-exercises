list_1 = [5, 10, 15, 20, 25, 50, 20]
new_item = 200
old_value = 20

def replace_item_in_list(list_1, old_value, new_item):
    index = list_1.index(old_value)
    list_1[index] = new_item

    return list_1


def main():
    print(replace_item_in_list(list_1, old_value, new_item))

if __name__ == "__main__":
   main()