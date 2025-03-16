# Problem 3: Souvenir Declutter
# As a time traveler, you've collected a mountain of souvenirs over the course of your travels. 
# You're running out of room to store them all and need to declutter. 
# Given a list of strings souvenirs and a integer threshold, declutter your souvenirs by writing a function declutter()
#  that returns a list of souvenirs strictly below threshold.
from collections import Counter
def declutter(souvenirs, threshold):
    sov_dict = Counter(souvenirs)
    # sov_dict = {}
    # for i in range(len(souvenirs)):
    #     if souvenirs[i] in sov_dict:
    #         sov_dict[souvenirs[i]]+= 1
    #     else:
    #         sov_dict[souvenirs[i]] = 1
    lst = [sovn for sovn, cont in sov_dict.items() if cont < threshold]  
    # for sovn, cont in sov_dict.items():
    #     if cont < threshold:
    #      lst.append(sovn)
    return lst
souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3
print(declutter(souvenirs1, threshold1))
souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2
print(declutter(souvenirs2, threshold2))
# Example Output:

# ["alien egg", "map", "map", "statue"]
# ["sword"]