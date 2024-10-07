# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current =None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val>list2.val:
            current = list2
            list2 =list2.next
        else:
            current=list1
            list1 = list1.next
        head =current
        while list1 and list2:
            print(list1.val,list2.val)
            if list1.val>list2.val:
                current.next = list2
                list2 =list2.next
            else:
                current.next =list1
                list1 = list1.next
            current = current.next
        while list1:
            current.next =list1
            list1 =list1.next
            current =current.next
        while list2:
            current.next =list2
            list2 =list2.next
            current =current.next
            
        return head       
            