class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create_ll(l):
        next1 = None
        for node in l[::-1]:
            if next1 is not None:
                prev = ListNode(node, next1)
            else:
                prev = ListNode(node)
            next1 = prev

        return next1

    @staticmethod
    def print_ll(head):
        print(ListNode.get_str_ll(head))

    @staticmethod
    def get_str_ll(head):
        if head is None:
            return "None"
        return str(head.val) + '->' + ListNode.get_str_ll(head.next)
