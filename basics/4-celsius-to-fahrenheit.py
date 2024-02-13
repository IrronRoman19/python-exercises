# Exercise 4 - Celsius or fahrenheit

c_or_f = input("Choose From Fahrenheit to Celsius(C) or Celsius to Farenheit(F), Choose with C or F:")


if c_or_f == "C" or c_or_f == "c":
    f = int(input("Enter Fahrenheit temperature: "))

    f_to_c = int((f - 32) * 5/9)
    print(f"Temperature in Fahrenheit: {f} °F", )
    print(f"Temperature in Celsius: {f_to_c} °C", )

elif c_or_f == "F" or c_or_f == "f":
    c = int(input("Enter Celsius temperature: "))

    c_to_f = int((c * 1.8) + 32)

    print(f"Temperature in Celsius: {c} °C", )
    print(f"Temperature in Fahrenheit: {c_to_f} °F", )
    
else:
    print("Please choose C or F")


