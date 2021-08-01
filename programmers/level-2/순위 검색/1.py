# 22:20~
def check(p, qr, check_list):
    escape = False

    for i in check_list:
        if escape:
            return False
        if i == 4:
            if int(p[i]) < int(qr[i]):
                escape = True
            else:
                continue
        else:
            if p[i] in qr[i] or qr[i] == '-':
                continue
            else:
                escape = True

    return not escape


def solution(info, query):
    queries = []
    answer = []
    for q in query:
        temp = q.split(' and ')
        food, score = temp[3].split(' ')[0], temp[3].split(' ')[1]
        temp[3] = food
        temp.append(score)
        queries.append(temp)

    for qr in queries:  # 1 이상 100,000 이하
        check_list = []
        for i in range(5):
            if qr[i] == '-':
                continue
            else:
                check_list.append(i)
        cnt = 0
        for p in info:  # 1 이상 50,000 이하
            p = p.split(' ')
            if check(p, qr, check_list):
                cnt += 1
        answer.append(cnt)

    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"]
query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

results = [1, 1, 1, 1, 2, 4]

print(solution(info, query))
