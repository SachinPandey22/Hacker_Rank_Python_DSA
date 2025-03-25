# Using the provided Node class below, create a linked list Tom Nook -> Tommy where 
# the instance tom_nook has value "Tom Nook" which points to the instance tommy that has value "Tommy".

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
timmy = Node("Timmy")
tom_nook.next = timmy
timmy.next = tommy
# print(tom_nook.value) 
# print(tom_nook.next.value) 
# print(tommy.value) 
# print(tommy.next) 
print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)
# Example Output:


# Tom Nook
# Tommy
# Tommy
# None