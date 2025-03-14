while True:
    N, M = map(int, input().split())

    if (N == 0 and M == 0):
        break

    calls = []
    for i in range(N):
        Source, Destination, Start, Duration = map(int, input().split())
        calls.append({"start" : Start, "end" : Start + Duration})

    for i in range(M):
        num_of_tap = 0
        Start, Duration = map(int, input().split())
        End = Start + Duration

        for call in calls:
            if call["start"] < End and call["end"] > Start:
                num_of_tap += 1

        print(num_of_tap)