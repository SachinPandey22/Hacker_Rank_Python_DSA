# Problem 3: Counting Unique Suits
# Some of Iron Man's suits are duplicates. 
# Given a list of strings suits where each string is a suit in Stark's collection,
# count the total number of unique suits in the list.

# Implement the solution iteratively.
# Implement the solution recursively.
# Discuss: what are the similarities between the two solutions? What are the differences?
# Evaluate the time complexity of each solution. Are they the same? 
# Define your variables and provide a rationale for why you believe your solution has the stated time complexity.
def count_suits_iterative(suits):
    count = 0
    list_suit = set(suits)
    for suit in list_suit: 
            count += 1
    return count
        
    

def count_suits_recursive(suits):
    if not suits:
        return 0
    first = suits[0]
    other_unique = count_suits_recursive(suits[1:])
    if first in suits[1:]:
        return other_unique
    else:
        return 1 + other_unique
    
    
print(count_suits_iterative(["Mark I", "Mark II", "Mark III", "Mark I"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Sachin", "Sapnil", "Saurav"]))

# # Example Output:

# # 3
# # 2