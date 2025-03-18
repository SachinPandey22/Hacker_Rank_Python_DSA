# Problem 2: Unique Travel Souvenirs
# As a seasoned traveler, you've collected a variety of souvenirs from different destinations.
#  You have an array of string souvenirs, where each string represents a type of souvenir.
#  You want to know if the number of occurrences of each type of souvenir in your collection is unique.

# Write a function that takes in an array souvenirs and returns True 
# if the number of occurrences of each value in the array is unique, or False otherwise.
from collections import Counter

def unique_souvenir_counts(souvenirs):
    counter_dic = Counter(souvenirs)
    counter_lst = list(counter_dic.values())
    return len(counter_lst) == len(set(counter_lst))


souvenirs1 = ["keychain", "hat", "hat", "keychain", "keychain", "postcard"]
souvenirs2 = ["postcard", "postcard", "postcard", "postcard"]
souvenirs3 = ["keychain", "magnet", "hat", "candy", "postcard", "stuffed bear"]

print(unique_souvenir_counts(souvenirs1))  
print(unique_souvenir_counts(souvenirs2)) 
print(unique_souvenir_counts(souvenirs3))
# Example Output:

# True
# Example 1 Explanation: The value "keychain" has 3 occurrences, "hat" has 2 
# and "postcard" has 1. No two values have the same number of occurrences.

# True
# Example 2 Explanation: The value "postcard" appears 4 times There's only one count (4), which is technically unique, so this should also return True.

# False
# Example 3 Explanation: Each item appears 1 time All counts are 1, which is not unique, so this should return False.
