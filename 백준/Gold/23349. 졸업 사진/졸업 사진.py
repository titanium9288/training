from collections import defaultdict


N = int(input())

students = set()
places = defaultdict(list)
timelines = defaultdict(list)
intervals = defaultdict(tuple)
earlist_peaks = defaultdict(int)

# 타임라인 길이 저장
max_timeline = 0

for _ in range(N):
    name, place, start, end = input().split()
    if name in students:
        continue

    students.add(name)
    places[place].append((int(start), int(end)))
    max_timeline = max(max_timeline, int(end))

# 타임라인에서 나올 수 있는 최대 사람 수 저장
max_people = 0

for place in sorted(places):
    timeline = [0] * (max_timeline + 2)

    # 차분배열, 누적합으로 계산 줄이기
    for start, end in places[place]:

        timeline[start] += 1
        timeline[end] -= 1

    for i in range(1, max_timeline):
        timeline[i] += timeline[i - 1]
        max_people = max(max_people, timeline[i])

    timelines[place] = timeline

# 가장 긴 구간 길이 저장
max_length = 0

for place in sorted(places):
    local_max_length = 0
    start = end = None
    current_start = None

    # 최대 사람 수에 맞지 않는다면 넘기기
    if max(timelines[place]) != max_people:
        continue

    # 슬라이딩 윈도우로 연속된 구간을 찾기
    for t in range(len(timelines[place])):
        # 가장 빨리 사람이 모이는 구간을 저장
        if timelines[place][t] == max_people:
            if earlist_peaks[place] == 0:
                earlist_peaks[place] = t
            if current_start is None:
                current_start = t
        else:
            if current_start is not None:
                if current_start <= earlist_peaks[place] < t:
                    current_length = t - current_start
                    if current_length > local_max_length:
                        local_max_length = current_length
                        start = current_start
                        end = t
                current_start = None

    # 마지막 구간 체크용
    if current_start is not None:
        if current_start <= earlist_peaks[place] < t:
            current_length = max_timeline + 1 - current_start
            if current_length > local_max_length:
                local_max_length = current_length
                start = current_start
                end = max_timeline

    intervals[place] = (start, end)
    max_length = max(local_max_length, max_length)

# 이제 사람 많은 순, 사전 순, 가장 빠른 순으로 사전 정렬해서 맨 앞의 값을 뽑으면 성공
# 다만, 사람 많은 순은 이미 필터링이 되어있으므로...
candidates = []

for place in sorted(intervals):
    earlist_peak = earlist_peaks[place]
    start, end = intervals[place]

    candidates.append((place, earlist_peak))

answer_place = sorted(candidates)[0][0]
print(answer_place, *intervals[answer_place])
