# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not k or not head or not head.next:
            return head
        # Get size of list, and place tail
        n = 1
        tail = head
        while tail.next:
            n += 1
            tail = tail.next
        # k should be less than n
        k %= n
        if k > 0:
            # head will always be after tail
            tail.next = head
            # New head is always going to n - k away for original head, and new tail is always n - k - 1
            for i in range(n - k - 1):
                head = head.next
            save = head.next
            head.next = None
            head = save
        return head
