# 15:34~16:09

def sharp_replace(str):
    return str.replace("C#", 'c').replace("D#", 'd').replace("F#", 'f').replace("G#", 'g').replace("A#", 'a')


def solution(m, musicinfos):
    answer = ''
    musics = []
    m = sharp_replace(m)
    for idx, info in enumerate(musicinfos):
        info = info.split(',')
        start = list(map(int, info[0].split(':')))
        end = list(map(int, info[1].split(':')))
        duration = end[0] * 60 + end[1] - (start[0] * 60 + start[1])
        music = sharp_replace(info[3])
        music_len = len(music)
        music = music * (duration // music_len) + music[:(duration % music_len)]
        if m in music:
            musics.append([info[2], -duration, idx])

    musics.sort(key=lambda x: (x[1], x[2]))

    if len(musics) == 0:
        answer = "(None)"
    else:
        answer = musics[0][0]

    return answer


m = [
    "ABCDEFG",
    "CC#BCC#BCC#BCC#B",
    "ABC"
]
musicinfos = [
    ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"],
    ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"],
    ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
]
for i, (s1, s2) in enumerate(zip(m, musicinfos)):
    print(f'case {i + 1} : {solution(s1, s2)}')
