# Problem 7: Check if Itinerary is Valid
# You are given an itinerary itinerary representing a list of trips between cities,
#  where each city is represented by an integer. We consider an itinerary valid if 
# it is a permutation of an itinerary template base[n].

# The template base[n] is defined as [1, 2, ..., n - 1, n, n] (in other words, 
# it is an itinerary of length n + 1 that visits cities 1 to n - 1 exactly once, 
# plus visits city n twice). For example, base[1] = [1, 1] and base[3] = [1, 2, 3, 3].

# Return True if the given itinerary is valid, otherwise return False.

# A permutation is an arrangement of a set of elements. For example [3, 2, 1] and [2, 3, 1] are
#  both possible permutations of the set of numbers 1, 2, and 3.
from collections import Counter
def is_valid_itinerary(itinerary):
    lst_dic = Counter(itinerary)
    max_num = max(itinerary)
    if len(itinerary) != max_num + 1:
        return False
    for i in range(1, max_num):
        if lst_dic[i] != 1:
            return False
    return lst_dic[max_num] == 2
    # lst = sorted(itinerary)
    # max_num = max(lst)
    # if len(lst) != max_num + 1:
    #     return False
    # for i in range(len(lst)):
    #     if lst[len(lst)-1] == lst[len(lst)-2] == max_num:
    #         return True
    # return False 

itinerary1 = [2, 1, 3]
itinerary2 = [1, 3, 3, 2]
itinerary3 = [1, 1]

print(is_valid_itinerary(itinerary1))
print(is_valid_itinerary(itinerary2))
print(is_valid_itinerary(itinerary3))
# Example Output:

# False
# Example 1 Explanation: Since the maximum element of the array is 3, 
# the only candidate n for which this array could be a permutation of base[n], 
# is n = 3. However, base[3] has four elements but array itinerary1 has three. 
# Therefore, it can not be a permutation of base[3] = [1, 2, 3, 3].
#  So the answer is false.

# True
# Example 2 Explanation:  Since the maximum element of the array is 3, the only 
# candidate n for which this array could be a permutation of base[n], is n = 3. It 
# can be seen that itinerary2 is a permutation of base[3] = [1, 2, 3, 3] 
# (by swapping the second and fourth elements in nums, we reach base[3]). 
# Therefore, the answer is true.

# True
# Example 3 Explanation; Since the maximum element of the array is 1, the only 
# candidate n for which this array could be a permutation of base[n], is n = 1. It 
# can be seen that itinerary3 is a permutation of base[1] = [1, 1]. Therefore, the
#  answer is true.