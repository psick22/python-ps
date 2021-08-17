from collections import Counter


def solution(gems):
    answer = []
    length = 2147000000
    left = 0
    right = 0
    type_length = len(Counter(gems))
    counter = Counter()
    while right < len(gems):
        counter.update([gems[right]])
        right += 1
        if len(counter) == type_length:
            while left < right:
                if counter[gems[left]] > 1:
                    counter.subtract([gems[left]])
                    left += 1
                elif length > right - left:
                    length = right - left
                    answer = [left + 1, right]
                    break
                else:
                    break

    return answer


gemgem = [
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
    ["AA", "AB", "AC", "AA", "AC"], ["XYZ", "XYZ", "XYZ"], ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

]

results = [
    [3, 7], [1, 3], [1, 1], [1, 5]
]

for gem in gemgem:
    print(solution(gem))
