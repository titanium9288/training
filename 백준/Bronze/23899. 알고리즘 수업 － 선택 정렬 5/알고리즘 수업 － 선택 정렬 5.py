N = int(input())

list_A = list(map(int, input().split()))
list_B = list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    
    if list_A == list_B:
        print(1)
        break

    max_idx = 0

    for j in range(i + 1):
        if list_A[j] > list_A[max_idx]:
            max_idx = j

    if i != max_idx:
        list_A[max_idx], list_A[i] = list_A[i], list_A[max_idx]

else:
    print(1 if list_A == list_B else 0)
