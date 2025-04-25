students = set(range(1, 31))

for i in range(28):
    students.remove(int(input()))

students = map(str, sorted(students))
print("\n".join(students))
