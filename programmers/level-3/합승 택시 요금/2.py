def solution(n, s, a, b, fares):
    # min(s->x + x->a + x->b)
    answer = float('inf')
    dis = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dis[i][i] = 0

    for x, y, cost in fares:
        dis[x][y] = cost
        dis[y][x] = cost

    # i -> k -> j
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            if dis[i][k] == float('inf'):
                continue
            for j in range(1, n + 1):
                if dis[k][j] == float('inf'):
                    continue
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, n + 1):
        answer = min(answer, dis[s][i] + dis[i][a] + dis[i][b])

    return answer


nn = [6, 7, 6]
ss = [4, 3, 4]
aa = [6, 4, 5]
bb = [2, 1, 6]

fares = [
    [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]],
    [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
]

for i, (n, s, a, b, fare) in enumerate(zip(nn, ss, aa, bb, fares)):
    print(solution(n, s, a, b, fare))
