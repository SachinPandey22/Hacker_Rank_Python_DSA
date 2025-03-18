# Problem 6: Most Popular Even Destination
# Given a list of integers destinations, where each integer represents the popularity score of a destination,
#  return the most popular even destination.

# If there is a tie, return the smallest one. If there is no such destination, return -1.
# from collections import Counter
def most_popular_even_destination(destinations):
    popular_even_dic = {}
    for dest in destinations:
        if dest % 2 == 0:
            if dest in popular_even_dic:
                popular_even_dic[dest] += 1
            else:
                popular_even_dic[dest] = 1
    popular =  -1
    max_count = 0
        
    for key, val in popular_even_dic.items():
        if val > max_count:
            popular = key
            max_count = val
    return popular

    # popularity_counter = Counter(destinations)
    # for key in list(popularity_counter.keys()):
    #     if key % 2 != 0:
    #         popularity_counter.pop("key", None)
    # max_count = max(list(popularity_counter.values()))
    # if max_count == 1:
    #     return -1
    # for key, val in popularity_counter.items():
    #     if val == max_count:
    #         return key


destinations1 = [0, 1, 2, 2, 4, 4, 1]
destinations2 = [4, 4, 4, 9, 2, 4]
destinations3 = [29, 47, 21, 41, 13, 37, 25, 7]

print(most_popular_even_destination(destinations1))
print(most_popular_even_destination(destinations2))
print(most_popular_even_destination(destinations3))
# Example Output:

# 2
# 4
# -1
