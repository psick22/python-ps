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
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        ts = hour * 60 + minute
        table.append(ts)

    table.sort(reverse=True)

    idx = 0
    while idx < len(bus_table):
        times = []
        temp = 0  # 해당 버스에 타는 인원
        while temp != m:
            if len(table) >= 1 and table[-1] <= bus_table[idx]:
                temp += 1
                times.append(table.pop())
            else:
                break

        # 버스가 끝났을때
        if idx == len(bus_table) - 1:
            if temp == m:  # 빈자리가 없을 때
                res = times.pop() - 1
                return toStr(res)
            else:  # 빈자리가 있을 때
                return toStr(bus_table[idx])

        idx += 1


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
