# Problem 6: Performances with Maximum Audience
# You are given an array audiences consisting of positive integers representing 
# the audience size for different performances at a music festival.

# Return the combined audience size of all performances in audiences with the maximum audience size.

# The audience size of a performance is the number of people who attended that performance.

def max_audience_performances(audiences):
    maxaud = max(audiences)
    total = 0
    for i in audiences:
        if i == maxaud:
            total += i
    return total
    # count_dict = {}
    # for count in audiences:
    #     if count in count_dict:
    #         count_dict[count] += 1
    #     else:
    #         count_dict[count] = 1
    # maxaud = max(count_dict.keys())
    # maxtotal = maxaud * count_dict[maxaud]
    # return maxtotal
    

audiences1 = [100, 200, 200, 250, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performances(audiences1))
print(max_audience_performances(audiences2))
# Example Output:

# 250
# 440