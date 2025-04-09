import math
import os
import random
import re
import sys
import ast

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to insert a node into a sorted linked list
def insert_sorted(head, value):
    new_node = ListNode(value)
    curr = head
    if not head:
        return new_node
    if head.val >= value:
        new_node.next = head
        return new_node
    while curr.next:
        if curr.next.val <= value:
            curr = curr.next
        else:
            break
    new_node.next = curr.next
    curr.next = new_node
    return head

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# ✅ Manual test runner — no changes to your functions
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 4], 3),
        ([1, 3, 5], 0),
        ([1, 2, 3], 4),
        ([], 5),
        ([2, 3, 4], 3),
        ([1, 2, 3], 1),
        ([1, 2, 3], 0),
    ]

    print("Running test cases for insert_sorted:\n")
    for idx, (lst, val) in enumerate(test_cases, 1):
        head = create_linked_list(lst)
        updated = insert_sorted(head, val)
        result = linked_list_to_list(updated)
        print(f"Test {idx}: insert {val} into {lst}")
        print("Result:", result)
        print("---")
