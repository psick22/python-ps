# https://programmers.co.kr/learn/courses/30/lessons/17678

def toStr(time):
    h = str(time // 60)
    mi = str(time % 60)
    if len(h) == 1:
        h = '0' + h
    if len(mi) == 1:
        mi = '0' + mi

    return f'{h}:{mi}'


def solution(n, t, m, timetable):
    # n회, t분 간격, m명씩
    bus_table = [60 * 9 + i * t for i in range(n)]
    table = []
    counter = {}
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        ts = hour * 60 + minute
        table.append(ts)

    table.sort()
    print(table)
    for ts in table:
        if ts not in counter.keys():
            counter[ts] = 1
        else:
            counter[ts] += 1

    for i, bus in enumerate(bus_table):
        temp = 0  # 버스에 타는 인원
        cnt = 0
        times = []
        while temp != m:
            if table[temp] <= bus:
                temp += 1
        for k, v in counter.items():
            if k <= bus:
                if temp + v <= m:
                    temp += v
                    counter[k] = 0
                    cnt += 1
                    times.append(k)
                else:
                    counter[k] -= (m - temp)
                    temp = m

        # 버스가 끝났을때
        if i == len(bus_table) - 1:
            if temp == m:  # 빈자리가 없을 때
                res = times.pop() - 1
                return toStr(res)
            else:  # 빈자리가 있을 때
                return toStr(bus)


        # 버스가 안끝났을때
        else:
            if cnt == len(counter.keys()):  # 버스가 안 끝났는데 사람들이 다탔을 때
                if temp < m:
                    return toStr(bus)
                else:
                    return toStr(bus + 60 * t)


nn = [1, 1, 2, 2, 1, 1, 10, 1, 2]
tt = [1, 1, 10, 1, 1, 1, 60, 1, 10]
mm = [1, 5, 2, 2, 5, 1, 45, 5, 3]

ttbs = [
    ["23:59"],
    ["08:00", "08:01", "08:02", "08:03"],
    ["09:10", "09:09", "08:00"],
    ["09:00", "09:00", "09:00", "09:00"],
    ["00:01", "00:01", "00:01", "00:01", "00:01"],
    ["23:59"],
    ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
     "23:59", "23:59", "23:59", "23:59"],
    ["00:00", "00:00", "00:00", "00:00", "00:01", "00:02", "00:03", "00:04"],
    ["09:05", "09:09", "09:13"]]

for i, (n, t, m, ttb) in enumerate(zip(nn, tt, mm, ttbs)):
    print(f'{i + 1} : {solution(n, t, m, ttb)}')
