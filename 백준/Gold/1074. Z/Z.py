def Z(size, row, col):
    length = 2**size

    if size == 0:
        return 0

    half = length // 2
    skip = half**2

    if r < row + half and c < col + half:
        return skip * 0 + Z(size - 1, row, col)
    elif r < row + half and c >= col + half:
        return skip * 1 + Z(size - 1, row, col + half)
    elif r >= row + half and c < col + half:
        return skip * 2 + Z(size - 1, row + half, col)
    else:
        return skip * 3 + Z(size - 1, row + half, col + half)


N, r, c = map(int, input().split())
print(Z(N, 0, 0))
