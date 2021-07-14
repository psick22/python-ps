import re


def solution(new_id: str):
    new_id = new_id.lower()
    new_id = re.sub('[^0-9a-z-._]', '', new_id)
    new_id = re.sub('(([.])\\2+)', '', new_id)
    new_id = new_id.strip('.')

    if len(new_id) == 0:
        new_id = 'aaa'

    elif len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')

    elif len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

id2 = 'a'
id = "=.="
print(solution(id))
