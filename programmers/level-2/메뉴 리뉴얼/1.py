from collections import Counter
import itertools as it


def solution(orders, course):
    answer = []
    cands = [[] for _ in range(len(course))]
    counters = []

    for i in range(len(orders)):
        orders[i] = ''.join(sorted(list(orders[i])))

    for o in orders:
        o = list(o)
        for idx, num in enumerate(course):
            for comb in it.combinations(o, num):
                cands[idx].append(''.join(comb))

    for i in range(len(cands)):
        counters.append(Counter(cands[i]))
    # print(counters)
    # print(counters[0].most_common())
    for i in range(len(course)):
        temp = []
        maxValue = 0

        for idx, item in enumerate(counters[i].most_common()):

            if idx == 0 and item[1] > maxValue:
                maxValue = item[1]
                temp.append(item)
            else:
                if item[1] == maxValue:
                    temp.append(item)

        for j in range(len(temp)):
            if temp[j][1] >= 2:
                answer.append(temp[j][0])

    return sorted(answer)


orders = [
    ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],
    ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],
    ["XYZ", "XWY", "WXA"]
]

course = [
    [2, 3, 4], [2, 3, 5], [2, 3, 4]
]

for o, c in zip(orders, course):
    print(f'({orders.index(o)}): {solution(o, c)}')
    print('======================================')

results = [
    ["AC", "ACDE", "BCFG", "CDE"],
    ["ACD", "AD", "ADE", "CD", "XYZ"],
    ["WX", "XY"]

]
