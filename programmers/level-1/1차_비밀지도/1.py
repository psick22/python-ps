# 16:37~16:59
def draw_map(arr):
    maps = [['0'] * n for _ in range(n)]
    for i, v in enumerate(arr):
        temp = list(map(int, format(v, 'b')))
        for j in range(n - 1, -1, -1):
            if len(temp) == 0:
                continue
            maps[i][j] = temp.pop()
    return maps


def solution(n, arr1, arr2):
    final = [['0'] * n for _ in range(n)]
    map1, map2 = draw_map(arr1), draw_map(arr2)
    for i in range(n):
        for j in range(n):
            if map1[i][j] == 1 or map2[i][j] == 1:
                final[i][j] = '#'
            else:
                final[i][j] = ' '

    for i, v in enumerate(final):
        final[i] = ''.join(v)

    return final


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
