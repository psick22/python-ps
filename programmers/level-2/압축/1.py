# 16:20~ 16:56

from collections import defaultdict


def initDict():
    dict = defaultdict(str)
    for i in range(26):
        dict[i + 1] = chr(i + 65)
    return dict


def getKey(value, dict):
    for k, v in dict.items():
        if value == v:
            return k
    return -1


def getNextKey(dict):
    return len(dict.keys()) + 1


def solution(msg):
    answer = []
    dict = initDict()
    i = 0
    while i < len(msg):
        for j in range(len(msg) - 1, i - 1, -1):
            if msg[i:j + 1] in dict.values():
                key = getKey(msg[i:j + 1], dict)
                answer.append(key)
                nextKey = getNextKey(dict)
                dict[nextKey] = msg[i:j + 2]
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
