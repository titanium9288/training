# 책 갯수 N, 박스 갯수 M
N, M = map(int, input().split())

if N != 0:
    books = list(map(int, input().split()))
    num_of_box = 1
    box_weight = 0

    for weight in books:
        # 책을 박스에 넣으려고 하는데, 박스에 넣으려는 책의 무게가 박스의 무게보다 크면
        if box_weight + weight > M:
            num_of_box += 1
            box_weight = 0
        box_weight += weight

    print(num_of_box)

else:
    print(0)
