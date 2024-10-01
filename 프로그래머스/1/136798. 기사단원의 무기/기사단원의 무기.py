def divisors(n):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:  
                result.append(n // i)
    return sorted(result)


def solution(number, limit, power):
    divisor_list = [len(divisors(i)) for i in range(1, number + 1)]
    
    return sum(power if i > limit else i for i in divisor_list)