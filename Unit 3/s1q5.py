# Problem 5: Content Cleaner
# You want to make sure your posts are clean and professional.
# Given a string post of lowercase and uppercase English letters, you want to remove any pairs of adjacent characters
# where one is the lowercase version of a letter and the other is the uppercase version of the same letter.
# Keep removing such pairs until the post is clean.

# A clean post does not have two adjacent characters post[i] and post[i + 1] where:

# post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
# Return the clean post.

# Note that an empty string is also considered clean.

def clean_post(post):
    stack = []
    for p in post:
        if stack and stack[-1] == p.swapcase():
            stack.pop()
        else:
            stack.append(p)
    return "".join(stack)
  

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
# Example Output:

# post

# s
