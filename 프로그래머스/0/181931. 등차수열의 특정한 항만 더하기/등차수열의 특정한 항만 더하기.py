def solution(a, d, included):
    sequence = range(a, a+(d*len(included)), d)
    return sum(sequence[i] for i in range(len(included)) if included[i])