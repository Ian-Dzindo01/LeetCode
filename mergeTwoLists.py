# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# create new list node object. Traverse
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        tail = res

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next            # use next value in next iteration
            else:
                tail.next = list2
                list2 = list2.next            # use next value in next iteration

            tail = tail.next        # iterate forward

        if list1:                 # if one of the lists is exhausted append the remainder of the list
            tail.next = list1
        elif list2:
            tail.next = list2

        return res.next

