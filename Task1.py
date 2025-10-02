# dictionary of students and their marks
students = {
    "Ayush": 85,
    "Rohit": 92,
    "Priya": 78,
    "Neha": 88,
    "Aman": 95
}

# ask user to enter student name
name = input("Enter student name: ")

# check if student exists in dictionary
if name in students:
    print(name, "got", students[name], "marks")
else:
    print("Sorry,", name, "not found in the record")
