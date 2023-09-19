possible_words = ['aya', 'ye', 'woo', 'ma']

def canBabble(word):
    for pw in possible_words:
        word = word.replace(pw, '1')
    return word.isdigit()


def solution(babbling):
    answer = 0
    for b in babbling:
        if  canBabble(b):
            answer += 1
    return answer