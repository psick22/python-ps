from collections import Counter


def solution(participant, completion):
    temp = Counter(participant) - Counter(completion)
    answer = list(temp.keys())[0]
    return answer


solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
