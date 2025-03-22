import sys

N, S, E = map(int, input().split())
total_damage = 0.0

for i in range(N):
    R, A, D = list(map(int, sys.stdin.readline().split()))
    unit_damage = D / A
    cycle_time = R + A

    section_start = (S // cycle_time) * A + max(0, min(S % cycle_time - R, A))
    section_end = (E // cycle_time) * A + max(0, min(E % cycle_time - R, A))

    duration = section_end - section_start

    total_damage += unit_damage * duration

print(total_damage / (E - S))
