# 16:20~ 16:56

from collections import defaultdict


def initDict():
    dict = defaultdict(str)
    for i in range(26):
        dict[i + 1] = chr(i + 65)
    return dict


def reverseDict():
    dict = defaultdict(int)
    for i in range(26):
        dict[chr(i + 65)] = i + 1
    return dict


def solution(msg):
    answer = []
    dict = initDict()
    rev = reverseDict()
    i = 0
    next = 27
    while i < len(msg):
        for j in range(len(msg) - 1, i - 1, -1):
            if msg[i:j + 1] in dict.values():
                key = rev[msg[i:j + 1]]
                answer.append(key)
                dict[next] = msg[i:j + 2]
                rev[msg[i:j + 2]] = next
                next += 1
                i = j
                break
        i += 1
    return answer


msg = [
    "KAKAO",
    "TOBEORNOTTOBEORTOBEORNOT",
    "ABABABABABABABAB"
]
answer = [
    [11, 1, 27, 15],
    [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
    [1, 2, 27, 29, 28, 31, 30]
]
for i, m in enumerate(msg):
    print(f'case {i + 1} : {solution(m)}')
