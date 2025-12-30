from solution import Solution, build_linked_list, linked_list_to_list


def run_tests():
    obj = Solution()

    test_num = 1
    list1 = [2, 4, 3]
    list2 = [5, 6, 4]
    list3 = [7, 0, 8]
    l1 = build_linked_list(list1)
    l2 = build_linked_list(list2)

    actual = obj.addTwoNumbers(l1, l2)
    expected = build_linked_list(list3)

    actual_list = linked_list_to_list(actual)
    expected_list = linked_list_to_list(expected)

    assert (
        actual_list == expected_list
    ), f"Test {test_num} failed, addTwoNumbers({l1}, {l2}) expected {expected_list} but returned {actual_list}."

    print(f"All {test_num} tests passed successfully!")


run_tests()
