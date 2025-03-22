from math import gcd, lcm


def is_possible(p1, p2, p3, x1, x2, x3):
    def check(a1, m1, a2, m2):
        return (a1 - a2) % gcd(m1, m2) == 0

    return check(x1, p1, x2, p2) and check(x1, p1, x3, p3) and check(x2, p2, x3, p3)


p1, p2, p3, x1, x2, x3 = map(int, input().split())

if is_possible(p1, p2, p3, x1, x2, x3):
    LCM = lcm(p1, p2, p3)

    for i in range(x1, LCM, p1):
        if i % p2 == x2 and i % p3 == x3:
            print(i)
            break
    else:
        print(-1)

else:
    print(-1)
