from ListNode import ListNode


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


def assert_linked_list_equal(actual, expected_values, test_name=""):
    """
    Compare a linked list to a plain Python list of values.
    Raises AssertionError with a helpful message if they differ.
    """
    actual_list = linked_list_to_list(actual)
    expected_list = list(expected_values)

    if actual_list != expected_list:
        prefix = f"[{test_name}] " if test_name else ""
        raise AssertionError(f"{prefix}Expected {expected_list} but got {actual_list}")
