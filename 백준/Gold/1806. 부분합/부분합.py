N, S = map(int, input().split())
num_array = list(map(int, input().split()))

# 투포인터
start = 0
end = 0
total = 0

min_length = float("inf")

while end < N:
    if total >= S:
        min_length = min(min_length, end - start)
        total -= num_array[start]
        start += 1
    else:
        total += num_array[end]
        end += 1

# 루프 종료 후, total이 S 이상인 경우에 대한 예외 처리
while total >= S:
    min_length = min(min_length, end - start)
    total -= num_array[start]
    start += 1

if min_length == float("inf"):
    print(0)
else:
    print(min_length)
