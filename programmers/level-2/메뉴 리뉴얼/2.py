import collections
import itertools


def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [k for k, v in most_ordered if v > 1 and v == most_ordered[0][1]]

    return [''.join(v) for v in sorted(result)]


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
