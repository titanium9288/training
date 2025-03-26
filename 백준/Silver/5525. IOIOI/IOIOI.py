
N = int(input())
P = 'I' + ('OI' * N)

M = int(input())
S = input()

answer = [n for n in range(len(S)) if S.find(P, n) == n]

print(len(answer))