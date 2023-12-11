students_count = int(input())
numbers = list(map(int, input().split()))

students = []

for number in numbers:
    students.insert(number, len(students) + 1)

print(' '.join(map(str, reversed(students))))