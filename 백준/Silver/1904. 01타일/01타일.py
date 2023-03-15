tile_list = [0, 1, 2]

n = int(input())

for i in range(2, n+1):
    if len(tile_list) > i:
        continue
    
    t1 = tile_list[i-1] % 15746
    t2 = tile_list[i-2] % 15746
    t3 = (t1 + t2) % 15746

    tile_list.append(t3)

print(tile_list[n])