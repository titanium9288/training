def hanoi(n, a=1, b=2, c=3, moves=[]):
    if n == 1:
        moves.append([a, c])
        return moves
    
    hanoi(n-1, a, c, b, moves)
    moves.append([a, c])
    hanoi(n-1, b, a, c)
    return moves


def solution(n):
    return hanoi(n)