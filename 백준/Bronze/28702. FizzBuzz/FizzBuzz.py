def FizzBuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return "FizzBuzz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0:
        return "Fizz"
    return n


s = []
for i in range(3):
    s.append(input())


for i in range(3):
    if s[i].isdigit():
        print(FizzBuzz(int(s[i]) + (3 - i)))
        break
