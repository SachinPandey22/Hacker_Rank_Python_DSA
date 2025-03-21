# Problem 7: Post Compare
# You often draft your posts and edit them before publishing.
# Given two draft strings draft1 and draft2, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will remain empty.

def post_compare(draft1, draft2):
    d1= []
    d2 = []
    for draft in draft1:
        if d1 and draft == "#":
            d1.pop()
        else:
            d1.append(draft)
    for draft in draft2:
        if d2 and draft == "#":
            d2.pop()
        else:
            d2.append(draft)
    return d1 == d2
       
  

print(post_compare("ab#c", "ad#c"))
print(post_compare("ab##", "c#d#")) 
print(post_compare("a#c", "b")) 
# Example Output:

# True
# True
# False