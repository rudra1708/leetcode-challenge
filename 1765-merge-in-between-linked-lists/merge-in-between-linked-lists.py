class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        first=list1
        for i in range(a-1):
            first=first.next
        second=first
        for i in range(b-a+2):
            second=second.next
        first.next=list2
        last=list2
        while last.next:
            last=last.next
        last.next=second
        return list1 