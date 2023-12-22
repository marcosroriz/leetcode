class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        list_head = ListNode()
        list_curr_element = ListNode()
        first = True
        while l1 != None or l2 != None:
            l1elem = 0 if l1 is None else l1.val
            l2elem = 0 if l2 is None else l2.val

            elem = l1elem + l2elem + extra
            new_elem = ListNode()
            if elem >= 10:
                extra = 1
                new_elem.val = elem - 10
            else:
                extra = 0
                new_elem.val = elem

            if first:
                first = False
                list_head = new_elem
                list_curr_element = new_elem
            else:
                list_curr_element.next = new_elem
                list_curr_element = new_elem

            if (l1 is not None):
                l1 = l1.next

            if (l2 is not None):
                l2 = l2.next

        if extra == 1:
            new_elem = ListNode(1)
            list_curr_element.next = new_elem

        return list_head
