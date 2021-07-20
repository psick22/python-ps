# 10:31~ 11:15
from collections import defaultdict


def solution(dirs):
    command = ['U', 'R', 'D', 'L']
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = defaultdict(list)
    p = (5, 5)
    cnt = 0
    for d in dirs:
        idx = command.index(d)
        nx = p[0] + dx[idx]
        ny = p[1] + dy[idx]
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            prev = (p[0], p[1])
            dest = (nx, ny)
            if dest in visited[f'{prev}']:
                p = dest
            else:
                visited[f'{prev}'].append(dest)
                visited[f'{dest}'].append(prev)
                p = dest
                cnt += 1

        else:
            continue

    return cnt


dirs = [
    "ULURRDLLU", "LULLLLLLU", "LRLRL"
]

for d in dirs:
    print(f'({dirs.index(d)}): {solution(d)}')
