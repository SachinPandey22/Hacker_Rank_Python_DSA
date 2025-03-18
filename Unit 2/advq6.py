# Problem 7: Lingual Frequencies
# As a time traveling linguist, you are analyzing texts written in an ancient script.
#  However, some words in the text are illegible and can't be deciphered.
#  Write a function find_most_frequent_word() that accepts a string text and a list of illegible words 
# illegibles and returns the most frequent word in text that is not an illegible word.

def find_most_frequent_word(text, illegibles):
    lst = text.lower().translate().split()
    count_dic = {}
    for wrd in lst:
        if wrd in count_dic and wrd not in illegibles:
            count_dic[wrd] += 1
        else:
            count_dic[wrd] = 1
    # max_count = max(count_dic.values())
    # for w, count in count_dic.items():
    #     if count == max_count:
    #         return w
    print(count_dic)
paragraph1 = "a."
illegibles1 = []
print(find_most_frequent_word(paragraph1, illegibles1)) 

paragraph2 = "Bob hit a ball, the hit BALL flew far after it was hit."
illegibles2 = ["hit"]
print(find_most_frequent_word(paragraph2, illegibles2)) 
# Example Output:

# a

# ball
# Example 2 Explanation:
# "hit" occurs 3 times, but it is an unknown word.
# "ball" occurs twice (and no other word does), so it is the most frequent legible word in the paragraph. 
# Note that words in the paragraph are not case sensitive,
# that punctuation is ignored (even if adjacent to words, such as "ball,"), 
# and that "hit" isn't the answer even though it occurs more because it is illegible.