from collections import defaultdict
import sys
sys.setrecursionlimit(300000)

answer = 0


def dfs(x, a, graph, visited):
    global answer
    visited[x] = 1

    for node in graph[x]:
        if not visited[node]:
            visited[node] = 1
            a[x] += dfs(node, a, graph, visited)
    answer += abs(a[x])
    return a[x]


def solution(a, edges):
    global answer

    if sum(a) != 0:
        return -1

    graph = defaultdict(list)
    visited = [0] * len(a)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dfs(0, a, graph, visited)

    return answer


aa = [[-5, 0, 2, 1, 2], [0, 1, 0]]
edges_list = [[[0, 1], [3, 4], [2, 3], [0, 3]], [[0, 1], [1, 2]]]

for i, (a, e) in enumerate(zip(aa, edges_list)):
    print(f'{i + 1} : {solution(a, e)}')
