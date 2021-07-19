# 12:40 ~ 12:54


def intersection(s1, s2):
    cnt = 0
    for item in set(s1):
        c1 = s1.count(item)
        c2 = s2.count(item)
        cnt += min(c1, c2)
    return cnt


def solution(str1, str2):
    set1 = []
    set2 = []
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            set1.append((str1[i] + str1[i + 1]).lower())
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            set2.append((str2[i] + str2[i + 1]).lower())
    inter = intersection(set1, set2)
    union = len(set1) + len(set2) - inter
    if union == 0:
        return 65536
    return int(inter / union * 65536)


str1 = [
    "FRANCE", "handshake", "aa1+aa2", "E=M*C^2"
]
str2 = [
    "french", "shake hands", "AAAA12", "e=m*c^2"
]
for i, (s1, s2) in enumerate(zip(str1, str2)):
    print(f'case {i + 1} : {solution(s1, s2)}')
