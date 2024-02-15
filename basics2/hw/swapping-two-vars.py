def swapping_variables(x, y):
   temp = x
   x = y
   y = temp

   return f"x = {x}\ny = {y}"

def main():
    print(swapping_variables(5, "Hello"))

if __name__ == "__main__":
   main()