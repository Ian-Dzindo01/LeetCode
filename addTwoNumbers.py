# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = [], []

        while(True):
            if l1 == None:
                break
            list1.append(l1.val)
            l1 = l1.next

        while(True):
            if l2 == None:
                break
            list2.append(l2.val)
            l2 = l2.next

        list1.reverse()
        list2.reverse()

        k = int(''.join(map(str,list1)))
        n = int(''.join(map(str,list2)))

        res = list(str(k+n))
        res.reverse()

        cur = dummy = ListNode(0)

        for e in res:
            cur.next = ListNode(e)
            cur = cur.next

        return dummy.next
