T = int(input())

for i in range(1, T + 1):
    a, b, c = sorted(map(int, input().split()))

    print(f"Scenario #{i}:")
    if c**2 == a**2 + b**2:
        print("yes")
    else:
        print("no")

    print()
