# 17:25~18:00


def solution(N, stages):
    ratio = [[i, 1] for i in range(N + 2)]
    total = [0] * (N + 2)
    count = [0] * (N + 2)
    for stage in stages:
        temp = stage
        count[stage] += 1
        while temp >= 0:
            total[temp] += 1
            temp -= 1
    for i in range(1, N + 1):
        if total[i] == 0:
            ratio[i][1] = 0
        else:
            ratio[i][1] = count[i] / total[i]

    answer = sorted(ratio[1:N + 1], key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]


N1 = 5
N2 = 2
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
stages2 = [1]
print(solution(N2, stages2))
