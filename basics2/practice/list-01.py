list_1 = [100, 200, 300, 400, 500]

def reverse_list(list_1):
    rev_list = []

    for i in list_1[::-1]:
        rev_list.append(i)
    
    return rev_list

def main():
    print(reverse_list(list_1))

if __name__ == "__main__":
   main()