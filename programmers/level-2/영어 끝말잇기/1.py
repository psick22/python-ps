# 00:23~00:37
def solution(n, words):
    seen = {}
    word_idx = -1
    seen[words[0]] = 1
    if len(words[0]) == 1:
        return [1, 1]

    for i in range(1, len(words)):
        if len(words[i]) == 1 or words[i] in seen or words[i][0] != words[i - 1][-1]:
            word_idx = i
            break

        seen[words[i]] = 1

    if word_idx == -1:
        return [0, 0]
    else:
        return [(word_idx % n) + 1, (word_idx // n) + 1]


nn = [3, 5, 2, 5, 5]

words = [
    ["k", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"],
    ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather",
     "refer", "reference", "estimate", "executive"],
    ["hello", "one", "even", "never", "now", "world", "draw"],
    ["hello", "hello"],
    ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "e", "establish", "hang", "gather",
     "refer", "reference", "estimate", "executive"]
]

results = [[3, 3], [0, 0], [1, 3]]

for n, word in zip(nn, words):
    print(solution(n, word))
