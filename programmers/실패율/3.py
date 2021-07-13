def solution(N, stages):
    ratio = [[i, 1] for i in range(N + 2)]
    total = len(stages)
    count = [0] * (N + 2)
    for stage in stages:
        count[stage] += 1

    for i in range(1, N + 1):
        if total == 0:
            ratio[i][1] = 0
        else:
            ratio[i][1] = count[i] / total
        total -= count[i]

    answer = sorted(ratio[1:N + 1], key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]


N1 = 5
N2 = 2
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
stages2 = [1]
print(solution(N1, stages1))
