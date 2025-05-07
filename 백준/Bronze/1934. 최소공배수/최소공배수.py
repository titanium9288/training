import math

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    gcd_a_b = math.gcd(a, b)

    print(a * b  // gcd_a_b)
    