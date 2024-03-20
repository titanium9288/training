import sys
import itertools


def calc_distance(s1, s2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def make_distance_pair():
    traits = [["I", "E"], ["S", "N"], ["T", "F"], ["J", "P"]]
    mbti_types = ["".join(p) for p in itertools.product(*traits)]
    distances = {}
    for trio in itertools.combinations_with_replacement(mbti_types, 3):
        trio_distance = sum(
            calc_distance(*pair) for pair in itertools.combinations(trio, 2)
        )
        distances[tuple(sorted(trio))] = trio_distance
    return distances


distances = make_distance_pair()

for _ in range(int(input())):
    N = int(sys.stdin.readline())
    students = list(sys.stdin.readline().split())

    # 각 유형의 수를 최대 3으로 제한
    student_dict = {mbti: min(students.count(mbti), 3) for mbti in set(students)}
    students = [mbti for mbti, count in student_dict.items() for _ in range(count)]

    min_distance = float("inf")
    for trio in itertools.combinations(students, 3):
        min_distance = min(min_distance, distances[tuple(sorted(trio))])

    sys.stdout.write(str(min_distance) + '\n')