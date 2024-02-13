list_1 = [1, 2, 3]

list_2 = ["Hello", "World"]

list_3 = [list_1, list_2]

list_4 = [1, "Hello", list_3]

print(list_1)
print(list_2)
print(list_3)
print(list_4)

print(list_1[0])
print(list_3[0][1])

print(len("banana"))



zoom_students = []

print(zoom_students)

# zoom_students.append("Roman Fesunenko")
# zoom_students.append(24)
zoom_students.append(["Roman Fesunenko", 24])

print(zoom_students)

# zoom_students.append("Ori Gez")
# zoom_students.append(21)
zoom_students.append(["Ori Gez", 21])

print(zoom_students)

print(f"First person is {zoom_students[0][0]} and his age is {zoom_students[0][1]}.")
print(f"Second person is {zoom_students[1][0]} and his age is {zoom_students[1][1]}.")