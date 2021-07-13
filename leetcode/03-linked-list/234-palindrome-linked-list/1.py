from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dq = deque()

        if not head:
            return True

        while head is not None:
            dq.append(head.val)
            head = head.next

        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False

        return True
