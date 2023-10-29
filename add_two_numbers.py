class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def get_next(self, l):
        if l is None:
            return None
        return l.next

    def get_val(self, l):
        if l is None:
            return 0
        return l.val

    def addTwoNumbers(self, l1, l2):
        nodes = []
        additional = 0
        while l1 is not None or l2 is not None:
            val = self.get_val(l1) + self.get_val(l2) + additional
            node = ListNode(val=val % 10)
            if nodes:
                nodes[-1].next = node
            nodes.append(node)
            additional = val // 10
            l1, l2 = self.get_next(l1), self.get_next(l2)
        if additional:
            node = ListNode(val=additional)
            nodes[-1].next = node
        return nodes[0] if nodes else None
