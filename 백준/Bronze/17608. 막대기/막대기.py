import sys

N = int(input())
sticks = []

for i in range(N):
    sticks += [int(sys.stdin.readline())]

max_length = 0
visible_sticks = 0
for stick in reversed(sticks):
    if stick > max_length:
        max_length = stick
        visible_sticks += 1

print(visible_sticks)
