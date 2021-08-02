# 22:20~
import itertools


def solution(info, query):
    answer = []
    map = {}
    for i in info:
        temp = i.split()
        conditions = temp[:-1]
        score = int(temp[-1])
        for j in range(5):
            for comb in list(itertools.combinations(conditions, j)):
                comb_key = ''.join(comb)
                if comb_key in map:
                    map[comb_key].append(score)
                else:
                    map[comb_key] = [score]

    for key in map.keys():
        map[key].sort()

    for q in query:
        q_temp = q.split(' and ')
        food, score = q_temp[3].split(' ')[0], q_temp[3].split(' ')[1]
        q_temp[3] = food
        q_conditions = q_temp
        q_score = int(score)

        while '-' in q_conditions:
            q_conditions.remove('-')
        q_key = ''.join(q_conditions)
        if q_key in map:
            scores = map[q_key]
            if len(scores) > 0:
                left, right = 0, len(scores),
                while left < right:
                    mid = (left + right) // 2
                    if scores[mid] >= q_score:
                        right = mid
                    else:
                        left = mid + 1
                answer.append(len(scores) - left)
        else:
            answer.append(0)
    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

results = [1, 1, 1, 1, 2, 4]

print(solution(info, query))
