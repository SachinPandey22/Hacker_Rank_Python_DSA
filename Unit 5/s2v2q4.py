# Write a function increment_ll() that takes in the head of a linked list of integer values and returns the same list, but with each node's value incremented by 1. Return the head of the list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def increment_ll(head):
    curr = head
    while curr:
        curr.value += 1
        curr = curr.next
    return head

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
print_linked_list(increment_ll(node_one))
# Example Output:

# 6 -> 7 -> 8