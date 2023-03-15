for testcase in range(int(input())):
    x, y = map(int, input().split())
    d = y - x

    for i in range(1, d+1):
        change = 0
        if i % 2 == 1:
            change = ((i+1)//2)**2
        else:
            change = i//2 * ((i//2)+1)
        
        if d <= change:
            print(i)
            break