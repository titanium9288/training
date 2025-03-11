N = int(input())
students = list(sorted(map(int, input().split()), reverse=True))

line1 = []
for i in range(len(students)):
    if not line1:
        line1.append(students[i])
        students[i] = 0
        continue

    if students[i] < line1[-1]:
        line1.append(students[i])
        students[i] = 0


line2 = []
for i in range(len(students)):
    if students[i] == 0:
        continue

    if not line2:
        line2.append(students[i])
        students[i] = 0
        continue

    if students[i] < line2[-1]:
        line2.append(students[i])
        students[i] = 0


print(len(line1) + len(line2)) 