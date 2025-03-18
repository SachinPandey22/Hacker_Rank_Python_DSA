# Problem 3: Secret Beach
# You make friends with a local at your latest destination, and they give you a coded message with the name of a secret beach most tourists don't know about! You are given the strings key and message which represent a cipher key and a secret message, respectively. The steps to decode the message are as follows:

# Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
# Align the substitution table with the regular English alphabet.
# Each letter in message is then substituted using the table.
# Spaces ' ' are transformed to themselves.
# For example, given key = "travel the world" (an actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('t' -> 'a', 'r' -> 'b', 'a' -> 'c', 'v' -> 'd', 'e' -> 'e', 'l' -> 'f', 'h' -> 'g', 'w' -> 'h', 'o' -> 'i', 'd' -> 'j').

# Write a function decode_message() that accepts the strings key and message and returns a string representing the decoded message.
import string
def decode_message(key, message):
    decode_dic = {}
    lst = []
    seen = set()
    i = 0
    for char in key:
        if char not in seen and char != " ":
            decode_dic[char] = string.ascii_lowercase[i]
            i += 1
            seen.add(char)
    for msg in message:
        if msg == " ":  # Preserve spaces
            lst.append(" ")
        else:
            lst.append(decode_dic[msg])

    return "".join(lst)
  

# # Substitution Table mapping 'the quick brown fox jumps over the lazy dog' to English alphabet

key1 = "the quick brown fox jumps over the lazy dog"
message1 = "vkbs bs t suepuv"

print(decode_message(key1, message1))
# Example Output 1:

# this is a secret
# Example Usage 2:

# Substitution Table mapping 'eljuxhpwnyrdgtqkviszcfmabo' to English alphabet

key2 = "eljuxhpwnyrdgtqkviszcfmabo"
message2 = "hntu depcte lxejw lxwntu zwx piqfx"

print(decode_message(key2, message2))
# Example Output 2:

# find laguna beach behind the grove