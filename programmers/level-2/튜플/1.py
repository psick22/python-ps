# 13:50~14:05
def solution(s):
    s = s[1:len(s) - 1].replace('{', '').replace('},', '/').replace('}', '').split('/')
    temp = sorted([list(map(int, i.split(','))) for i in s], key=len)

    answer = []
    for item in temp:
        for num in item:
            if not num in answer:
                answer.append(num)
    return answer


params = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"
]

for s in params:
    print(f'({params.index(s)}): {solution(s)}')
    print('======================================')

results = [
    [2, 1, 3, 4], [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1]
]
