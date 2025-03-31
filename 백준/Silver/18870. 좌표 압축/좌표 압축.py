N = int(input())
pos = list(map(int, input().split()))

unique_pos = sorted(set(pos))
compressed_dict = {}

for i in range(len(unique_pos)):
    compressed_dict[unique_pos[i]] = i

answer = [compressed_dict[p] for p in pos]
print(*answer)
