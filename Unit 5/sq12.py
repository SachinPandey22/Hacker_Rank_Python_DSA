# Write a function print_list() that takes in the head of a linked list and returns a string linking together 
# the values of the list with the separator "->".

# Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def print_list(head):
    values =[]
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return " -> ".join(values)
        

isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

print(print_list(isabelle))
# Example Output:

# Isabelle -> Saharah -> C.J.