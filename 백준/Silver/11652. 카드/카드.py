counter = {}

for i in range(int(input())):
    num = int(input())
    if num not in counter:
        counter[num] = 0
    
    counter[num] += 1

max_count = max(counter.values())
max_count_card = min([num for num, count in counter.items() if count == max_count])

print(max_count_card)