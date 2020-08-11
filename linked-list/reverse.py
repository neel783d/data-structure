from node import ListNode


def reverse_ll_stack(head):
    """
    Reverses Linked List using stack
    :param head: head of LinkedList
    :return: Reversed head
    """
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr)
        next1 = curr.next
        curr.next = None
        curr = next1

    top = None
    new_head = None
    while len(stack) != 0:
        curr = stack.pop()
        if new_head is None:
            new_head = curr
            top = curr
        else:
            top.next = curr
            top = top.next
    return new_head


def reverse_ll_two_ptr(head):
    """
    Reverse LL using two pointers
    :param head: head of LL
    :return: head of new LL
    """
    new_head = None
    curr = head
    while curr is not None:
        next1 = curr.next
        curr.next = new_head
        new_head = curr
        curr = next1
    return new_head


def reverse_ll_recurse(head):
    """
    Head Recursion
    :param head:
    :return:
    """
    if head is None or head.next is None:
        return head

    rest = reverse_ll_recurse(head.next)
    head.next.next = head
    head.next = None
    return rest


def test_reverse_ll_stack():
    head = ListNode.create_ll([1, 2, 3, 4, 5])
    print('old: {}'.format(ListNode.get_str_ll(head)))
    new_head = reverse_ll_stack(head)
    print('new: {}'.format(ListNode.get_str_ll(new_head)))


def test_reverse_ll_two_ptr():
    head = ListNode.create_ll([1, 2, 3, 4, 5])
    print('old: {}'.format(ListNode.get_str_ll(head)))
    new_head = reverse_ll_two_ptr(head)
    print('new: {}'.format(ListNode.get_str_ll(new_head)))


def test_reverse_ll_recurse():
    head = ListNode.create_ll([1, 2, 3, 4, 5])
    print('old: {}'.format(ListNode.get_str_ll(head)))
    new_head = reverse_ll_recurse(head)
    print('new: {}'.format(ListNode.get_str_ll(new_head)))


if __name__ == "__main__":
    test_reverse_ll_stack()
    test_reverse_ll_two_ptr()
    test_reverse_ll_recurse()
