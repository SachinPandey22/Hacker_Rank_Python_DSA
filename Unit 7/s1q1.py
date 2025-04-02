# # Problem 1: Counting Iron Man's Suits
# # Tony Stark, aka Iron Man, has designed many different suits over the years. 
# # Given a list of strings suits where each string is a suit in Stark's collection, count 
# # the total number of suits in the list.

# # Implement the solution iteratively without the use of the len() function.
# # Implement the solution recursively.
# # Discuss: what are the similarities between the two solutions? What are the differences?
def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    return 1 + count_suits_iterative(suits[1:])
    
    
print(count_suits_iterative(["Mark I", "Mark II", "Mark III", "Sachin"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV", "Sachin"]))
# # Example Output:

# # 3
# # 4