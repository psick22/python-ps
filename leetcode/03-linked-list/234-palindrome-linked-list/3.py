from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: ListNode) -> bool:
    if not head or not head.next:
        return True

    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True
