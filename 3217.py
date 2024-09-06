QUESTION:
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.
SOLUTION:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not nums:
            return head  
        nums=set(nums)  
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        while cur.next:
            if cur.next.val in nums:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next
