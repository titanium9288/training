def fibonacci(A, n):
    # 0일 땐 항등행렬을 반환
    if n == 0:
        return [[1, 0], [0, 1]]

    # 1일 땐 초기행렬 반환
    if n == 1:
        return A

    half = fibonacci(A, n // 2)
    result = multiple_matrix(half, half)

    if n % 2 == 0:
        return result
    else:
        return multiple_matrix(result, A)


# 2*2 행렬곱
def multiple_matrix(A, B):
    result = [[0, 0], [0, 0]]

    result[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % 1000000007
    result[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % 1000000007
    result[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % 1000000007
    result[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % 1000000007

    return result


N = int(input())
print(fibonacci([[1, 1], [1, 0]], N)[1][0])
