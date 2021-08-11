import re
import datetime


def get_start_time(day_str, end, duration):
    year, month, day = list(map(int, day_str.split('-')))
    h, m, s, ms = list(map(int, re.split('[:.]', end)))
    dur_s, dur_ms = list(map(int, duration))

    end_dt = datetime.datetime(year, month, day, h, m, s, ms * 1000)
    end_ts = int(end_dt.timestamp() * 1000)

    start_dt = (end_dt - datetime.timedelta(seconds=dur_s, milliseconds=dur_ms - 1))
    start_ts = int(start_dt.timestamp() * 1000)

    return start_ts, end_ts


def solution(lines):
    #  초당 최대 처리량 = 요청의 응답 완료 여부에 관계없이 임의 시간부터 1초간 처리하는 요청의 최대 개수
    new_logs = []

    for l in lines:
        d, end_time, dur = l.split(' ')

        temp = dur.rstrip('s').split('.')
        if len(temp) == 1:
            temp.append(0)
        start_ts, end_ts = get_start_time(d, end_time, temp)
        new_logs.append([start_ts, end_ts])

    new_logs.sort(key=lambda x: x[0])

    count = 0

    for i in range(len(new_logs)):
        temp = set()

        for j in range(len(new_logs)):
            if new_logs[j][0] <= new_logs[i][1] < new_logs[j][1]:
                temp.add(j)
            elif new_logs[i][1] <= new_logs[j][1] < new_logs[i][1] + 1000:
                temp.add(j)
            elif new_logs[i][1] <= new_logs[j][0] < new_logs[i][1] + 1000:
                temp.add(j)

        count = max(count, len(temp))

    return count


llines = [
    [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ],
    [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ],
    [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]

]

for i, lines in enumerate(llines):
    print(f'{i + 1} : {solution(lines)}')
