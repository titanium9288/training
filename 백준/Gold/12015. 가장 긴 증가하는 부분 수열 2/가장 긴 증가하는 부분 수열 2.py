from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

sub_array = []

# 이분 탐색을 통한 i의 위치 찾기
# 이 경우, LIS의 실제 수열은 보장할 수 없지만 "길이"는 보장할 수 있다.

for i in A:
    index = bisect_left(sub_array, i)

    if index == len(sub_array):
        sub_array.append(i)
    else:
        sub_array[index] = i

print(len(sub_array))