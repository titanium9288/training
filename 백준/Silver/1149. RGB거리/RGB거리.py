N = int(input())
dp = []

for i in range(N):
    R, G, B = map(int, input().split())

    RGB_dict = {"R": R, "G": G, "B": B}
    if i != 0:
        RGB_dict["R"] = min(dp[i - 1]["G"], dp[i - 1]["B"]) + R
        RGB_dict["G"] = min(dp[i - 1]["R"], dp[i - 1]["B"]) + G
        RGB_dict["B"] = min(dp[i - 1]["R"], dp[i - 1]["G"]) + B
    dp.append(RGB_dict)

print(min(dp[-1].values()))
