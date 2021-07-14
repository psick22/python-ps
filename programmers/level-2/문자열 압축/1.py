# 1시간
def solution(s):
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):
        res = ''
        temp = s[0:i]
        cnt = 1
        for j in range(i, len(s), i):
            if temp == s[j:j + i]:
                cnt += 1
            else:
                if cnt > 1:
                    res += str(cnt)
                res += temp
                temp = s[j:j + i]
                cnt = 1
        if cnt > 1:
            res += str(cnt)
        res += temp
        answer = min(answer, len(res))
    return answer

s = "aabbaccc"
print(solution(s))
