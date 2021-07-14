# 17:21~ 18:12
def isRight(s):
    cnt = 0
    for char in s:
        if char == '(':
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return cnt == 0


def reverse(s):
    s = list(s)
    for i in range(len(s)):
        if s[i] == '(':
            s[i] = ')'
        else:
            s[i] = '('
    return ''.join(s)


def solution(p):
    if len(p) == 0:
        return p
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:  # 가장 작은 균형잡힌 문자열
            u = p[:i + 1]
            v = p[i + 1:]
            break

    if isRight(u):
        return f'{u}{solution(v)}'
    else:
        return f'({solution(v)}){reverse(u[1:-1])}'


params = [
    "(()())()", ")(", "()))((()"
]

for p in params:
    print(solution(p))
