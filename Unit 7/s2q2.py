# Problem 2: Collecting Infinity Stones
# Thanos is collecting Infinity Stones.
# Given an array of integers stones representing the power of each stone, 
# return the total power using a recursive approach.

# Evaluate the time complexity of your solution. 
# Define your variables and provide a rationale for why you believe your solution has the 
# stated time complexity.

def sum_stones(stones):
    if not stones:
        return 0
    return stones[0] + sum_stones(stones[1:])
print(sum_stones([5, 10, 15, 20, 25, 30]))
print(sum_stones([12, 8, 22, 16, 10]))
# # Example Output:

# # 105
# 68