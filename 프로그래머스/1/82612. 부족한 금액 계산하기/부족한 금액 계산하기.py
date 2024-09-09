def solution(price, money, count):
    money -= sum(range(price, price*count+1, price))
    return -money if money < 0 else 0