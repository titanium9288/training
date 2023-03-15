# 24416

def fibo(n):
    fList = [1, 1]
    for i in range(2, n):
        fList.append(fList[i - 1] + fList[i-2])
    return fList[n-1]

N = int(input())
print(fibo(N), N-2)