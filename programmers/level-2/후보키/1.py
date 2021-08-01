# 20:40~21:23
import itertools


def isUnique(cols, relation):
    s = set()

    for row in relation:
        temp = []
        for i in cols:
            temp.append(row[i])
        s.add(''.join(temp))

    if len(s) == len(relation):
        return True
    else:
        return False


def isMinimal(cols, candidates):
    is_minimal = True
    for cand in candidates:
        if cand in itertools.combinations(cols, len(cand)):
            is_minimal = False
    return is_minimal


def solution(relation):
    candidates = []
    len_col = len(relation[0])
    iterable = [i for i in range(len_col)]
    for r in range(1, len_col + 1):
        combs = list(itertools.combinations(iterable, r))
        for cols in combs:
            if cols in candidates:
                continue
            else:
                is_unique = isUnique(cols, relation)
                is_minimal = isMinimal(cols, candidates)
                if is_unique and is_minimal:
                    candidates.append(cols)

    return len(candidates)


relation = [
    ["100", "ryan", "music", "2"],
    ["200", "apeach", "math", "2"],
    ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"],
    ["500", "muzi", "music", "3"],
    ["600", "apeach", "music", "2"]
]

print(solution(relation))
