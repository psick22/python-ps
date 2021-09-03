from collections import deque


def strToSecond(time):
    h, m, s = list(map(int, time.split(':')))
    return h * 3600 + m * 60 + s


def secondToStr(second):
    s = second % 60
    second = second // 60
    m = second % 60
    second = second // 60
    h = second

    res = []
    for x in [h, m, s]:
        if x < 10:
            res.append(f'0{x}')
        else:
            res.append(str(x))

    return ':'.join(res)


def solution(play_time, adv_time, logs):
    play_time = strToSecond(play_time)
    adv_time = strToSecond(adv_time)
    times = [0 for _ in range(play_time + 1)]

    for log in logs:
        s, e = log.split('-')
        s = strToSecond(s)
        e = strToSecond(e)
        times[s] += 1
        times[e] -= 1

    for i in range(play_time):
        times[i] += times[i - 1]

    best = 0
    sum = 0
    idx = 0

    dq = deque()
    for i in range(adv_time):
        sum += times[i]
        dq.append(times[i])
    best = sum

    for i in range(adv_time, play_time):
        sum += times[i]
        dq.append(times[i])
        sum -= dq.popleft()
        if sum > best:
            idx = i - adv_time + 1
            best = sum

    answer = secondToStr(idx)
    return answer


play_times = ["02:03:55", "99:59:59", "50:00:00"]
adv_times = ["00:14:15", "25:00:00", "50:00:00"]
logs_list = [
    ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],
    ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],
    ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]

for i, (p, a, l) in enumerate(zip(play_times, adv_times, logs_list)):
    print(f'{i + 1}: {solution(p, a, l)}')
