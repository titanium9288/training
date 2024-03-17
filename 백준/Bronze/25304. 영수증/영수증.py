total_price = int(input())
n = int(input())
calc_price = 0

for i in range(n):
    price, count = map(int, input().split())
    calc_price += price * count

if calc_price == total_price:
    print("Yes")
else:
    print("No")