# 하루를 초로 나타낸 상수
SECONDS_IN_A_DAY = 24 * 60 * 60


def time_to_sec(f_time: str) -> int:
    '''
    HH:MM:SS 형태로 받은 시간을 int 타입의 초로 변환해서 return 합니다.
    '''

    # 시간을 초로 변환
    f_hour, f_min, f_sec = map(int, f_time.split(":"))
    return f_hour * 3600 + f_min * 60 + f_sec


def sec_to_time(sec: int) -> str:
    '''
    int 타입으로 받은 초를 HH:MM:SS 형태로 변환해서 return 합니다.
    '''

    # 음수로 들어온 시간을 양수로 변환
    sec = sec if sec > 0 else sec + SECONDS_IN_A_DAY
    f_hour, f_min, f_sec = sec // 3600, (sec % 3600) // 60, sec % 60

    # 시간을 문자열로 변환
    return f"{f_hour:02d}:{f_min:02d}:{f_sec:02d}"
    

# 현재 시간
# current_time = "13:52:30"
current_time_in_sec = time_to_sec(input())

# 시작 시간
# start_time = "14:00:00"
start_time_in_sec = time_to_sec(input())

# 초로 변환한 시간을 문자열로 변환
remain_time_str = sec_to_time(start_time_in_sec - current_time_in_sec)

# 시간 출력
print(remain_time_str)
