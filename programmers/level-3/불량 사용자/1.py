import itertools


def check(cases, banned_id):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(cases[i]):
            return False
        else:
            for j in range(len(banned_id[i])):
                if banned_id[i][j] == "*":
                    continue
                elif banned_id[i][j] != cases[i][j]:
                    return False
    return True


def solution(user_id, banned_id):
    res = []
    ban_len = len(banned_id)
    perms = list(itertools.permutations(user_id, ban_len))
    for cases in perms:
        if check(cases, banned_id):
            cases = set(cases)
            if cases not in res:
                res.append(cases)

    answer = len(res)

    return answer


users = [
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["frodo", "fradi", "crodo", "abc123", "frodoc"]
]

banned = [["fr*d*", "abc1**"], ["*rodo", "*rodo", "******"], ["fr*d*", "*rodo", "******", "******"]]

results = [2, 2, 3]

for u, b in zip(users, banned):
    print(solution(u, b))
