def solution(s):
    s = sorted(list(map(int, s.split())))
    return ' '.join((str(min(s)), str(max(s))))