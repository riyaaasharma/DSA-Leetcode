# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        dummy = ListNode(0)
        new_head = dummy
        sum_val = 0

        # Skip the initial zero node
        current = current.next

        while current is not None:
            if current.val != 0:
                sum_val += current.val
            else:
                if sum_val != 0:
                    new_node = ListNode(sum_val)
                    dummy.next = new_node
                    dummy = dummy.next
                    sum_val = 0
            current = current.next

        return new_head.next
            