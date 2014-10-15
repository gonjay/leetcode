# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head is None:
            return None
        fast = head
        slow = head
        while fast and slow:
            slow = slow.next
            fast = fast.next
            if fast is not None:
                fast = fast.next
            if slow == fast:
                break
        if fast is None:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast