list_1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
def remove_empty_strings(list_1):
    for i in list_1:
        if i == "":
            list_1.remove(i)
        else:
            pass

    return list_1

def main():
    print(remove_empty_strings(list_1))

if __name__ == "__main__":
   main()