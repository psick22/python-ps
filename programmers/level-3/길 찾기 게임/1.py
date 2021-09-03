import sys

sys.setrecursionlimit(200000)


class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None


def create(tree):
    tree.sort(key=lambda x: (x[2], x[1]))
    num, x, y = tree.pop()
    node = Node(num)
    print(node.num)
    left = []
    right = []
    for i in range(len(tree)):
        if tree[i][1] > x:
            right.append(tree[i])
        else:
            left.append(tree[i])

    if left:
        node.left = create(left)
    if right:
        node.right = create(right)

    return node


def preorder(node, answer):
    answer.append(node.num)
    if node.left:
        preorder(node.left, answer)
    if node.right:
        preorder(node.right, answer)
    return answer


def backorder(node, answer):
    if node.left:
        backorder(node.left, answer)
    if node.right:
        backorder(node.right, answer)
    answer.append(node.num)
    return answer


def solution(nodeinfo):
    tree = [[i + 1] + v for i, v in enumerate(nodeinfo)]
    node = create(tree)

    pre = preorder(node, [])
    back = backorder(node, [])

    return [pre, back]


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
print(solution(nodeinfo))
