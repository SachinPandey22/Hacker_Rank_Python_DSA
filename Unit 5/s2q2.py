# Connect the provided node instances below to create the linked list kk_slider -> harriet -> saharah -> isabelle.

# A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.

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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle
# Add code here to link the above nodes
# Example Usage:

print_linked_list(kk_slider)
# Example Output:

# K.K. Slider -> Harriet -> Saharah -> Isabelle