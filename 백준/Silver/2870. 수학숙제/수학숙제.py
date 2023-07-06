import re

N = int(input())
paper = ""
for _ in range(N):
    paper += "a" + input()

paper = re.findall(r"\d+", paper)
paper = list(sorted([int(i) for i in paper]))
for i in paper:
    print(i)
