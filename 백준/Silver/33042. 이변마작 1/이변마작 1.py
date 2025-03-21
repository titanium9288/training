N = int(input())
tiles = input().split()

tile_count = {}
event = 0

for i in range(len(tiles)):
    tile = tiles[i]

    if tile not in tile_count:
        tile_count[tile] = 0

    tile_count[tile] += 1

    if tile_count[tile] >= 5:
        event = i + 1
        break

print(event)
