# 12:06~ 12:49

answer = [0, 0]


def solution(arr):
    rhalf = int(len(arr) / 2)
    chalf = int(len(arr[0]) / 2)

    arr_sum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr_sum += arr[i][j]

    if arr_sum == 0:
        answer[0] += 1
    elif arr_sum == len(arr) ** 2:
        answer[1] += 1
    elif len(arr) != 1:
        sub1 = [row[:chalf] for row in arr[:rhalf]]
        sub2 = [row[chalf:] for row in arr[:rhalf]]
        sub3 = [row[:chalf] for row in arr[rhalf:]]
        sub4 = [row[chalf:] for row in arr[rhalf:]]
        subs = [sub1, sub2, sub3, sub4]
        for sub in subs:
            solution(sub)

    return answer


arr = [

    [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]]

for s in arr:
    print(f'({arr.index(s)}): {solution(s)}')
