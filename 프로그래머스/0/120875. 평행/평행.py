def get_parallel(dot1, dot2, dot3, dot4):
    return (dot2[0] - dot1[0]) * (dot4[1] - dot3[1]) == (dot2[1] - dot1[1]) * (dot4[0] - dot3[0])

def solution(dots):
    dot1, dot2, dot3, dot4 = dots
    
    slopes = [
        get_parallel(dot1, dot2, dot3, dot4),
        get_parallel(dot1, dot3, dot2, dot4),
        get_parallel(dot1, dot4, dot2, dot3)
    ]
    
    return int(any(slopes))
    