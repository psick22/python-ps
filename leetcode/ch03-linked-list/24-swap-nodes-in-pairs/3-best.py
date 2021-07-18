class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            ptr = head.next
            head.next = self.swapPairs(ptr.next)
            ptr.next = head
            return ptr

        return head
