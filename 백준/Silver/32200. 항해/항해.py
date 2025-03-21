N, X, Y = map(int, input().split())
sandwiches = list(map(int, input().split()))

answer_piece = 0
trash = 0

for sandwich in sandwiches:

    if sandwich < X:
        trash += sandwich
        continue

    pieces = sandwich // X
    answer_piece += pieces

    max_size = pieces * Y
    if sandwich <= max_size:
        left_sandwich = 0
    else:
        left_sandwich = sandwich - max_size

    trash += left_sandwich

print(answer_piece)
print(trash)
