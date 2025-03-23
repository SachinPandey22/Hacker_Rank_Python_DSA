# Problem 3: Arrange Event Attendees by Priority
# You are organizing a large event and need to arrange the attendees based on their priority levels. You are given a 0-indexed list attendees, where each element represents the priority level of an attendee, and an integer priority that indicates a particular level of priority.

# Your task is to rearrange the attendees list such that the following conditions are met:

# Every attendee with a priority less than the specified priority appears before every attendee with a priority greater than the specified priority.
# Every attendee with a priority equal to the specified priority appears between the attendees with lower and higher priorities.
# The relative order of the attendees within each priority group (less than, equal to, greater than) must be preserved.
# Return the attendees list after the rearrangement.

def arrange_attendees_by_priority(attendees, priority):
    left_pointer = 0
    right_pointer = len(attendees) - 1
    while left_pointer < right_pointer:
        while attendees[left_pointer] < priority and left_pointer <= right_pointer:
            left_pointer += 1
        while attendees[right_pointer] > priority and left_pointer < right_pointer:
            right_pointer -= 1
        if left_pointer < right_pointer:
            temp = attendees[right_pointer]
            attendees[right_pointer] = attendees[left_pointer]
            attendees[left_pointer] = temp
            left_pointer += 1
            right_pointer -= 1 


    return attendees

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 
# Example Output:

# [9,5,3,10,10,12,14]
# [-3,2,4,3]