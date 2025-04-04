# Problem 4: Puzzling it Out
# A new witness has emerged and provided a new account of events the night of the crime.
# Given the heads of two sorted linked lists, known_timeline and witness_timeline,
# each representing a numbered sequence of events, merge the two timelines into one sorted sequence of events. T
# he resulting linked list should be made by splicing together the nodes of the first two timelines. 
# Return the head of the merged timeline.

# Evaluate the time and space complexity of your solution.
# Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

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

def merge_timelines(known_timeline, witness_timeline):
    dummy = Node(0)
    dummy_head = dummy
    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            dummy_head.next = known_timeline
            known_timeline = known_timeline.next
        else:
            dummy_head.next = witness_timeline
            witness_timeline = witness_timeline.next
        dummy_head = dummy_head.next
    if  witness_timeline:
            dummy_head.next = witness_timeline
    else:
            dummy_head.next = known_timeline
    return dummy.next


known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))

print_linked_list(merge_timelines(known_timeline, witness_timeline))
# Example Output:

# 1 -> 1 -> 2 -> 3 -> 4 -> 4