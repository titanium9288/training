import sys


class Set:
    def __init__(self):
        self.set = [False] * 21

    def add(self, n):
        self.set[n] = True

    def remove(self, n):
        self.set[n] = False

    def check(self, n):
        return str(int(self.set[n]))

    def toggle(self, n):
        self.set[n] = not self.set[n]

    def all(self):
        self.set = [True] * 21

    def empty(self):
        self.set = [False] * 21


S = Set()
output = []

for i in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == "add":
        S.add(int(command[1]))
    elif command[0] == "remove":
        S.remove(int(command[1]))
    elif command[0] == "check":
        sys.stdout.write(S.check(int(command[1])) + '\n')
    elif command[0] == "toggle":
        S.toggle(int(command[1]))
    elif command[0] == "all":
        S.all()
    elif command[0] == "empty":
        S.empty()