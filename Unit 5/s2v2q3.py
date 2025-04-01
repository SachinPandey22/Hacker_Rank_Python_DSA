# Problem 3: Insert Node as Second Element
# Write a function add_second() that takes in the head of a linked list and a value val as parameters. 
# It should insert val as the second node in the linked list and return the head of the linked list. 
# (You can assume head is not None.)

# Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.

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

def add_second(head, val):
    new_node = Node(val)
    new_node.next = head.next    
    head.next = new_node
    return head

    
    

original_list_head = Node("banana")
second = Node("blue shell")
third = Node("bullet bill")
original_list_head.next = second
second.next = third


# Linked list: "banana" -> "blue shell" -> "bullet bill"
new_list = add_second(original_list_head, "red shell")
print_linked_list(new_list)
# Example Output:

# banana -> red shell -> blue shell -> bullet bill
