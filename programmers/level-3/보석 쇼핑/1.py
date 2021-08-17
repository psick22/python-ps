from collections import Counter


def solution(gems):
    counter = Counter(gems)
    n = len(counter)
    m = len(gems)
    for length in range(n, m + 1):
        for idx in range(0, m - n + 1):
            c = Counter(gems[idx:idx + length])
            if len(c) == n:
                return [idx+1, idx + length]


gemgem = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"], ["XYZ", "XYZ", "XYZ"], ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

]

results = [
    [3, 7], [1, 3], [1, 1], [1, 5]
]

for gem in gemgem:
    print(solution(gem))
