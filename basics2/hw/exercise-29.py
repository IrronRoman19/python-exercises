color_list_1 = {"White", "Black", "Red"}
color_list_2 = {"Red", "Green"}

def search_non_present_list(color_list_1, color_list_2):
    total_colors = set()

    for i in color_list_1:
        total_colors.add(i)

    for i in color_list_2:
        total_colors.add(i)

    for i in color_list_2:
        total_colors.remove(i)

    print(total_colors)

            
def main():
    search_non_present_list(color_list_1, color_list_2)

if __name__ == "__main__":
   main()