import sys
input = sys.stdin.readline

N = int(input())
vertexes = [tuple(map(int, input().split())) for _ in range(N)]
vertexes.append(vertexes[0])

answer = 0
for i in range(N):
    x1, y1 = vertexes[i]
    x2, y2 = vertexes[i + 1]

    # 신발끈 공식
    answer += (x1 * y2) - (x2 * y1)

print(abs(answer) / 2)
