def calc_charge(money, coin):
    return money // coin, money % coin


for _ in range(int(input())):
    money = int(input())

    for coin in [25, 10, 5, 1]:
        charge, money = calc_charge(money, coin)
        print(charge, end=" ")
    print()