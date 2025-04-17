T = int(input())

for _ in range(T):
    N = int(input())

    if N % 8 != 0:
        print("No")
        continue

    count = 0
    while N != 0 and count < 8:
        number_of_8 = int("8" * len(str(N)))
        
        if number_of_8 > N:
            number_of_8 = int("8" * (len(str(N)) - 1))

        q, r = divmod(N, number_of_8)

        count += q
        N = r

    if N != 0 or count > 8:
        print("No")
    else:
        print("Yes")
