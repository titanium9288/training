N = int(input())

dist = [list(map(int, input().split())) for _ in range(N)]
answer = float("inf")

for start_color in ["R", "G", "B"]:
    # 리스트 컴프리헨션으로 처리하려고 했는데, 지저분해졌음
    # 나중에 수정 할 기회나 아이디어가 있다면...
    dp = [
        {
            "RGB"[i]: dist[0][i] if "RGB"[i] == start_color else float("inf")
            for i in range(3)
        }
    ]

    for i in range(1, N):
        R, G, B = dist[i]
        RGB_dict = {"R": R, "G": G, "B": B}
        RGB_dict["R"] = min(dp[i - 1]["G"], dp[i - 1]["B"]) + R
        RGB_dict["G"] = min(dp[i - 1]["R"], dp[i - 1]["B"]) + G
        RGB_dict["B"] = min(dp[i - 1]["R"], dp[i - 1]["G"]) + B
        dp.append(RGB_dict)

    # N번 집과 i번 집이 같지 않아야 하므로
    end_color = list({"R", "G", "B"} - {start_color})
    answer = min(dp[-1][end_color[0]], dp[-1][end_color[1]], answer)

print(answer)
