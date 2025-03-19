# Problem 6: Pair Contestants
# In a reality TV challenge, contestants must be paired up in teams.
#  Each team's combined score must be divisible by a target number k. 
# You are given an array of integers scores representing the scores of the contestants and an integer k.

# You need to determine whether it is possible to pair all contestants such that the sum of the scores of each pair is divisible by k.

# Return True if it is possible to form the required pairs, otherwise return False.
from collections import Counter
def pair_contestants(scores, k):
    rem_count = Counter(score % k for score in scores)
    if len(scores) % 2 != 0:
        return False
    if rem_count[0] % 2 != 0:
        return False
    if k % 2 == 0:
        if rem_count[k//2] % 2 != 0:
            return False
    for i in rem_count:
        complement = (k - i) % k
        if rem_count[i] != rem_count[complement]:
         return False
    return True


    

scores1 = [1,2,3,4,5,10,6,7,8,9]
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3)) 
# Example Output:

# True
# True
# False