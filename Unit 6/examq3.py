#!/bin/python

import math
import os
import random
import re
import sys
import ast

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next
    
# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    temp = ListNode()
    current = temp
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return temp.next

#
# Do not change this function
#
def longer_list(head1, head2):
    curr1 = head1
    curr2 = head2
    while curr1 and curr2:
        curr1 = curr1.next
        curr2 = curr2.next
    if curr2:
        return head2
    else:
        return head1

# ✅ Test cases added below
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [4, 5]),        # head1 is longer
        ([1], [2, 3, 4]),           # head2 is longer
        ([9, 9], [7, 7]),           # equal length → return head1
        ([], [1]),                  # head1 empty
        ([42], []),                # head2 empty
        ([], []),                   # both empty
    ]

    print("Running test cases for longer_list():\n")
    for i, (list1, list2) in enumerate(test_cases, 1):
        h1 = create_linked_list(list1)
        h2 = create_linked_list(list2)
        result = longer_list(h1, h2)
        print(f"Test Case {i}:")
        print("Input List 1:", list1)
        print("Input List 2:", list2)
        print("Longer List: ", end="")
        print_linked_list(result)
        print("---")
