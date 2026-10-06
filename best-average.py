students = {
    "Ali": 18.5,
    "Sara": 19.2,
    "Reza": 17.8,
    "Mina": 19.7
}

best_student = ""
best_average = 0

for name in students:
    if students[name] > best_average:
        best_average = students[name]
        best_student = name

print("Best student:", best_student)
print("Average:", best_average)