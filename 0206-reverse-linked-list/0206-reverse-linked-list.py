# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next   # Store next node
            curr.next = prev        # Reverse the link
            prev = curr             # Move prev forward
            curr = next_node        # Move curr forward

        return prev