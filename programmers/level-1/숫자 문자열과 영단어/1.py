map = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def solution(s):
    for i in map.keys():
        if i in s:
            s = s.replace(i, str(map[i]))

    return int(s)


s = "one4seveneight"
print(solution(s))
