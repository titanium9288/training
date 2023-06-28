import sys 

C = int(input())

for _ in range(C):
    N = list(map(int, sys.stdin.readline().split()))[1:]
    avg = sum(N) / len(N)
    cnt = sum(1 for i in N if i > avg)
    print(f'{cnt / len(N) * 100:.3f}%')