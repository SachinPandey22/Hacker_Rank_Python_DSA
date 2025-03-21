# Problem 1: Post Format Validator
# You are managing a social media platform and need to ensure that posts are properly formatted. 
# Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
# You are given a string representing a post's content, and your task is to determine 
# if the tags in the post are correctly formatted.

# A post is considered valid if:

# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.
def is_valid_post_format(posts):
    open_tag = ["(", "{", "["]
    close_tag = [ ")", "}", "]"]
    open_close_dic = dict(zip(close_tag, open_tag))
    stack_trace = []
    for tag in posts:
        if tag in open_tag:
            stack_trace.append(tag)
        elif tag in close_tag:
            
            if stack_trace and stack_trace[-1] == open_close_dic[tag]:
                stack_trace.pop()
            else:
                return False
    return len(stack_trace) == 0

print(is_valid_post_format("()"))       # True
print(is_valid_post_format("()[]{}"))   # True
print(is_valid_post_format("(]"))       # False
print(is_valid_post_format("([{}])"))   # True
print(is_valid_post_format("(({})]"))   # False
print(is_valid_post_format(")("))       # False
print(is_valid_post_format("((("))      # False
print(is_valid_post_format(""))  
# Example Output:

# True
# True
# False
