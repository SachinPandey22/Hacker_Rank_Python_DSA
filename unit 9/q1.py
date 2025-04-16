from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, key=None, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def build_tree(values):
    if not values:
        return None

    def get_key_value(item):
        if isinstance(item, tuple):
            return item[0], item[1]
        else:
            return None, item

    key, value = get_key_value(values[0])
    root = TreeNode(value, key)
    queue = deque([root])
    index = 1

    while queue:
        node = queue.popleft()
        if index < len(values) and values[index] is not None:
            left_key, left_value = get_key_value(values[index])
            node.left = TreeNode(left_value, left_key)
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            right_key, right_value = get_key_value(values[index])
            node.right = TreeNode(right_value, right_key)
            queue.append(node.right)
        index += 1

    return root

def merge_orders(order1, order2):
    if not order1:
        return order2
    if not order2:
        return order1

    new_root = TreeNode(order1.val + order2.val)
    new_root.left = merge_orders(order1.left, order2.left)
    new_root.right = merge_orders(order1.right, order2.right)
    return new_root

# Example usage
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

print_tree(merge_orders(order1, order2))


# #Problem 2: Croquembouche - Print flavors in level order

# # class Puff:
# #     def __init__(self, flavor, left=None, right=None):
# #         self.val = flavor
# #         self.left = left
# #         self.right = right

# # def print_design(design):
# #     if not design:
# #         return []
    
# #     queue = deque([design])
# #     result = []
    
# #     while queue:
# #         node = queue.popleft()
# #         result.append(node.val)
        
# #         if node.left:
# #             queue.append(node.left)
# #         if node.right:
# #             queue.append(node.right)
    
# #     print(result)
# # croquembouche = Puff("Vanilla", 
# #                     Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
# #                     Puff("Strawberry"))
# # print_design(croquembouche)


# #Problem 3: Maximum Tiers in Cake

# # class TreeNode():
# #      def __init__(self, value, left=None, right=None):
# #         self.val = value
# #         self.left = left
# #         self.right = right

# # def max_tiers(cake):
# #     if not cake:
# #         return 0
# #     left_search = max_tiers(cake.left)
# #     right_search = max_tiers(cake.right)
    
# #     return 1 + max(left_search, right_search)





# # # Using build_tree() function included at top of page
# # cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# # cake = build_tree(cake_sections)

# # print(max_tiers(cake))


# # #

# #Problem 4: Maximum Tiers in Cake II

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#         self.val = value
#         self.left = left
#         self.right = right

# def max_tiers(cake):
#     if not cake:
#         return 0
#     queue = queue([cake])

#     while queue:
#         le


    




# # Using build_tree() function included at top of page
# cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
# cake = build_tree(cake_sections)

# print(max_tiers(cake))
