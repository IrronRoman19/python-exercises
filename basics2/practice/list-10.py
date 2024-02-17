list_1 = [5, 20, 15, 20, 25, 50, 20]
removing_value = 20

def remove_items_from_list(list_1, removing_value):
    for i in list_1:
        if i == removing_value:
            list_1.remove(removing_value)
        else:
            pass
    
    return list_1

def main():
    print(remove_items_from_list(list_1, removing_value))

if __name__ == "__main__":
   main()