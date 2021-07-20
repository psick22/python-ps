# 17:33~18:16

def solution(skill, skill_trees):
    answer = 0
    tree_list = [skill[:i] for i in range(len(skill) + 1)]
    print(tree_list)
    for tree in skill_trees:
        temp = ''
        for i in range(len(tree)):
            if tree[i] in list(skill):
                temp += tree[i]
        if temp in tree_list:
            answer += 1

    return answer


skill = ["CBD"]
skill_trees = [["BACDE", "CBADF", "AECB", "BDA"]]
for i, (s1, s2) in enumerate(zip(skill, skill_trees)):
    print(f'case {i + 1} : {solution(s1, s2)}')
