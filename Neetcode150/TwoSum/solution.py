from typing import Optional
from lc_utils.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        # Loop until both lists are done and no carry remains
        while l1 or l2 or carry != 0:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            total = x + y + carry
            carry = total // 10
            newVal = total % 10

            curr.next = ListNode(newVal)
            curr = curr.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next

def build_linked_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr