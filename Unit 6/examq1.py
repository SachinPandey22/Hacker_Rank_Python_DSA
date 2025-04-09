#!/bin/python

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

def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next


#
# Complete the 'create_linked_list' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_ARRAY values as parameter.
#

def create_linked_list(values):
    head = None
    tail = None
    for i in values:
        node = ListNode(i)
        if not head:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head
    # Write your code here

# ✅ TEST CASES ADDED HERE:
if __name__ == '__main__':
    test_cases = [
        [1, 2, 3],
        [10],
        [],
        [5, 6, 7, 8, 9],
        [0, 0, 0],
    ]

    print("Running create_linked_list test cases:\n")
    for idx, values in enumerate(test_cases, 1):
        print(f"Test case {idx}: Input = {values}")
        head = create_linked_list(values)
        print("Output:", end=" ")
        print_linked_list(head)
        print("---")
