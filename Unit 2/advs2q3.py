# Problem 3: Cows and Bulls
# In a reality TV show, contestants play a mini-game called Bulls and Cows for a prize. 
# The objective is to guess a secret number within a limited number of attempts.
#  You, as the host, need to provide hints to the contestants based on their guesses.

# When a contestant makes a guess, you provide a hint with the following information:

# The number of "bulls," which are digits in the guess that are in the correct position.
# The number of "cows," which are digits in the guess that are in the secret number but are located in the wrong position.
# Given the secret number secret and the contestant's guess guess, return the hint for their guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows.
#  Note that both secret and guess may contain duplicate digits.

def get_hint(secret, guess):
    sec_dic = dict(enumerate(secret))
    x= 0
    y = 0
    lst = list(sec_dic.values())
    for i in range(len(guess)):
        if guess[i] == sec_dic[i]:
            x += 1
            lst.remove(sec_dic[i])
        elif guess[i] in lst:
            y += 1
            lst.remove(guess[i])
    return f"{x}A{y}B"

    

secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))
# Example Output:

# 1A3B
# Example 1 Explanation: 
# Bulls are connected with a '|' and cows are marked with an asterisk:
# "1807"
#   |
# "7810"
#  * **

# 1A1B
# Example 2 Explanation:
# Bulls are connected with a '|' and cows are marked with an asterisk:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
#    *              *
# Note that only one of the two unmatched 1s is counted as a cow since the 
# non-bull digits can only be rearranged to allow one 1 to be a bull.