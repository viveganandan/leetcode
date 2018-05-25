# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newhead = head
        if head and head.next:
            newhead = head.next
        prev = None
        while head and head.next:
            save = head.next.next
            head.next.next = head
            if prev:
                prev.next = head.next
            head.next = save
            prev = head
            head = save
        return newhead
