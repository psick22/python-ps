# 6분
def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    unknown_cnt = 0
    cnt = 0
    for x in lottos:
        if x == 0:
            unknown_cnt += 1
        if x in win_nums:
            cnt += 1
    best = cnt + unknown_cnt
    worst = cnt

    return [rank[best], rank[worst]]


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))
