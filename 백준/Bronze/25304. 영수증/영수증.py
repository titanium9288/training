total_price = int(input())
n = int(input())

for i in range(n):
    price, count = map(int, input().split())
    total_price -= price * count

if total_price:
    print("No")
else:
    print("Yes")