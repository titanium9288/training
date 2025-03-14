answer = 0
N, M = map(int, input().split())

subjects = []
for i in range(N):
    Pi, Li = map(int, input().split())
    students = list(map(int, input().split()))

    if Li > Pi:
        subjects.append(1)
        continue

    students.sort()
    subjects.append(students[Pi - Li])

subjects.sort()

for subject in subjects:
    if M < subject:
        break
    
    M -= subject
    answer += 1

print(answer)