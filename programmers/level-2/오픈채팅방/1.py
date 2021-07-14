# 13:28~13:48
from collections import defaultdict


def solution(record):
    res = []  # [cmd, uid]
    id_map = {}
    commands = ["Enter", "Leave", "Change"]
    for log in record:
        log = log.split()
        cmd = commands.index(log[0])
        res.append([cmd, log[1]])
        if cmd == 0:
            id_map[log[1]] = log[2]
        elif cmd == 2:
            id_map[log[1]] = log[2]
    answer = []
    for x in res:
        if x[0] == 0:
            answer.append(f'{id_map[x[1]]}님이 들어왔습니다.')
        elif x[0] == 1:
            answer.append(f'{id_map[x[1]]}님이 나갔습니다.')

    return answer

record = ["Enter uid1234 Muzi",
          "Enter uid4567 Prodo",
          "Leave uid1234",
          "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]
print(solution(record))