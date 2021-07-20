# 14:05~14:36
def solution(files):
    answer = []
    temp = []
    for idx, v in enumerate(files):
        i = 0
        number = 0
        head = ''
        tail = ''
        while i < len(v):
            if v[i].isdigit():
                j = i + 1
                while j < len(v) and v[j].isdigit():
                    j += 1
                head = v[:i].lower()
                number = int(v[i:j])
                i = j

            elif v[i] == '.':
                tail = v[i:].lower()
                break

            else:
                i += 1
        temp.append((idx, head, number, tail))
    if temp:
        temp.sort(key=lambda x: (x[1], x[2], x[0]))
    for x in temp:
        answer.append(files[x[0]])

    return answer


files = [
    ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"],
    ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"],
    ["img000012345", "img1.png", "img2", "IMG02"]
]

for f in files:
    print(f'case {files.index(f)} : {solution(f)}')
