def time_to_sec(time):
    time_min, time_sec = map(int, time.split(":"))
    return time_min * 60 + time_sec

def sec_to_time(sec):
    time_min, time_sec = sec//60, sec%60
    return f"{time_min:02}:{time_sec:02}"

def solution(video_len, pos, op_start, op_end, commands):
    
    video_time = time_to_sec(video_len)
    pos_time = time_to_sec(pos)
    
    op_start_time = time_to_sec(op_start)
    op_end_time = time_to_sec(op_end)
    
    if op_start_time <= pos_time <= op_end_time:
        pos_time = op_end_time
    
    for command in commands:
        if command == "next":
            pos_time = min(video_time, pos_time + 10)
        if command == "prev":
            pos_time = max(0, pos_time - 10)
            
        if op_start_time <= pos_time <= op_end_time:
            pos_time = op_end_time
        
    return sec_to_time(pos_time)