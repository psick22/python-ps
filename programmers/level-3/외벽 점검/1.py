from itertools import permutations


def solution(n, weak, dist):
    linear = weak + [w + n for w in weak]
    answer = []
    for i, s in enumerate(weak):
        for perm in permutations(dist):
            count = 1
            ptr = s
            for friend in perm:
                ptr += friend
                if ptr < linear[i - 1 + len(weak)]:
                    count += 1
                    ptr = [w for w in linear[i + 1:i - len(weak)] if w > ptr][0]
                else:
                    answer.append(count)
                    break

    if not answer:
        return -1
    else:
        return min(answer)


## [1, 5, 6, 10] + [1+12, 5+12, 6+12, 10+12]

nn = [12, 12]
weaks = [[1, 5, 6, 10], [1, 3, 4, 9, 10]]
dists = [[1, 2, 3, 4], [3, 5, 7]]
results = [2, 1]

for i, (n, w, d) in enumerate(zip(nn, weaks, dists)):
    print(f'{i + 1} : {solution(n, w, d)}')
