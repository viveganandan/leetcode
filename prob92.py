# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = head
        prev = None
        # Find the starting node that we should start reversing at
        for _ in range(1, m):
            prev = start
            start = start.next
        # Reverse starting from m to n
        cur = start
        for _ in range(m, n + 1):
            save = cur.next
            cur.next = prev
            prev = cur
            cur = save
        # Hook the node previous to start with last node in reversed window
        if start.next:
            start.next.next = prev
        else:
            head = prev
        start.next = cur
        return head
